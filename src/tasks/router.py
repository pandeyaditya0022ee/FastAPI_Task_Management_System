from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.utils.helpers import is_authenticated
from src.user.models import UserModel
from typing import List


task_router = APIRouter(prefix="/tasks")

@task_router.post("/create",status_code=status.HTTP_201_CREATED,response_model=TaskResponseSchema)
def create_task(body : TaskSchema, db:Session = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.create_task(body,db,user)


@task_router.get("/list_task",status_code=status.HTTP_200_OK,response_model=List[TaskResponseSchema])
def get_all_tasks (db:Session = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.get_tasks(db,user)

@task_router.get("/one_task/{task_id}",status_code=status.HTTP_200_OK,response_model=TaskResponseSchema)
def get_one_task(task_id : int,db:Session = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.get_specific_task(task_id,db)

@task_router.put("/update/{task_id}",status_code=status.HTTP_201_CREATED,response_model=TaskResponseSchema)
def update_task(body : TaskSchema,task_id:int,db:Session = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.update_task(body,task_id,db,user)


@task_router.delete("/delete/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id : int,db:Session = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.delete_task(task_id,db,user)