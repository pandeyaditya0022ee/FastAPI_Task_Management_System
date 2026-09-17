from fastapi import APIRouter , status,Depends,Request,BackgroundTasks
from src.user import controller
from src.user.dtos import UserSchema, UserResponseSchema, LoginSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session



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