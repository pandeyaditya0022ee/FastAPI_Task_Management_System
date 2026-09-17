from fastapi import APIRouter , status,Depends,Request,BackgroundTasks
from src.user import controller
from src.user.dtos import UserSchema, UserResponseSchema, LoginSchema , UpdateSchema
from src.user.models import UserModel
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.utils.helpers import is_authenticated



user_router = APIRouter(prefix="/user")

@user_router.post("/register",response_model= UserResponseSchema,status_code=status.HTTP_201_CREATED)
async def regester(body:UserSchema,bg_task : BackgroundTasks,db:Session = Depends(get_db)):
    return await controller.register(body,db,bg_task)


@user_router.post("/login",status_code=status.HTTP_200_OK)
def user_login(body :LoginSchema,db:Session = Depends(get_db)):
    return controller.login(body,db)

@user_router.get("/is_auth",response_model=UserResponseSchema,status_code=status.HTTP_200_OK)
def is_auth(request : Request,db:Session =Depends(get_db)):
    return controller.is_authenticated(request,db)

@user_router.delete("/delete/{user_id}",status_code=status.HTTP_200_OK)
def delete_user(user_id:int,db:Session=Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.delete_user(user_id,db,user)

@user_router.put("/update/{user_id}",response_model=UserResponseSchema,status_code=status.HTTP_200_OK)
def update_user(body:UpdateSchema,user_id:int,db:Session = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.update_user(body,user_id,db,user)