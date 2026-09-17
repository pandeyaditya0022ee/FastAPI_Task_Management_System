from src.user.models import UserModel
from fastapi import HTTPException, status, Request,Depends
from sqlalchemy.orm import Session
import jwt
from jwt.exceptions import InvalidTokenError
from src.utils.settings import settings
from datetime import datetime
from src.utils.db import get_db

def is_authenticated(request: Request, db: Session = Depends(get_db)):
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
