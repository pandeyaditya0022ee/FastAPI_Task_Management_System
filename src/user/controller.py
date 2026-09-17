from src.user.models import UserModel
from fastapi import HTTPException, status, Request,BackgroundTasks
from src.user.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
import jwt
from jwt.exceptions import InvalidTokenError
from src.utils.settings import settings
from datetime import datetime, timedelta
from src.utils.mail import email_send

password_hash = PasswordHash.recommended()


def get_password_hash(password):
    return password_hash.hash(password)


def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


async def register(body: UserSchema, db: Session,bg_task:BackgroundTasks):
    # validationg user
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(status_code=400, detail="Username Already Exist.....")
    is_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_email:
        raise HTTPException(status_code=400, detail="Email Already Exist.....")

    hash_password = get_password_hash(body.password)

    new_user = UserModel(
        name=body.name,
        username=body.username,
        hash_password=hash_password,
        email=body.email,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    #sending mail
    # await email_send([new_user.email])
    bg_task.add_task(email_send,[new_user.email])
    

    return new_user


def login(body: LoginSchema, db: Session):
    user = db.query(UserModel).filter(UserModel.username == body.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You Entring Wrong username",
        )

    if not verify_password(body.password, user.hash_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You Entring Wrong Password",
        )

    exp_time = datetime.now() + timedelta(minutes=settings.EXPIRATION_TIME)
    token = jwt.encode(
        {"username": user.username, "exp": exp_time},
        settings.SECRET_KEY,
        settings.ALGORITHM,
    )

    return {"token": token}


def is_authenticated(request: Request, db: Session):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="You Are Unauthoroized"
            )

        token = token.split(" ")[-1]

        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        username = data.get("username")
        exp_time = data.get("exp")

        current_time = datetime.now().timestamp()

        if current_time > exp_time:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="You Are Unauthoroized"
            )

        user = db.query(UserModel).filter(UserModel.username == username).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="You Are Unauthoroized"
            )

        return user
    
    except InvalidTokenError:
        raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED, detail="You Are Unauthoroized"
                    )
