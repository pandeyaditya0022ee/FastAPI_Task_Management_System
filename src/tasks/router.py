from fastapi import APIRouter, Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db


task_router = APIRouter(prefix="/tasks")

@task_router.post("/create")
def create_task(body : TaskSchema, db = Depends(get_db)):
    return controller.create_task(body,db)


@task_router.get("/list_task")
def get_all_tasks(db = Depends(get_db)):
    return controller.get_tasks(db)

@task_router.get("/one_task/{task_id}")
def get_one_task(task_id : int,db = Depends(get_db)):
    return controller.get_specific_task(task_id,db)

@task_router.put("/update/{task_id}")
def update_task(body : TaskSchema,task_id:int,db = Depends(get_db)):
    return controller.update_task(body,task_id,db)


@task_router.delete("/delete/{task_id}")
def delete_task(task_id : int,db = Depends(get_db)):
    return controller.delete_task(task_id,db)