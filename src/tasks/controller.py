from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException
from sqlalchemy import select
from src.user.models import UserModel


def create_task(body: TaskSchema, db: Session, user: UserModel):
    data = body.model_dump()
    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        is_complete=data["is_complete"],
        user_id=user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_tasks(db: Session,user : UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    
    return tasks


def get_specific_task(task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=" Task Not Found")

    return task


def update_task(body: TaskSchema, task_id: int, db: Session,user:UserModel):
    task :TaskModel = db.query(TaskModel).get(task_id)

    if not task:
        raise HTTPException(status_code=404, detail=" Task Not Found")
    
    if task.user_id != user.id:
                raise HTTPException(status_code=401, detail="You are Unauthroize ")


    # task.title = body.title
    # task.description = body.description
    # task.is_complete = body.is_complete

    body = body.model_dump(exclude_unset=True)

    for key, value in body.items():
        setattr(task, key, value)

    db.add(task)
    db.commit()
    db.refresh(task)

    return  task


def delete_task(task_id: int, db: Session,user : UserModel):
    task:TaskModel = db.query(TaskModel).get(task_id)

    if not task:
        raise HTTPException(status_code=404, detail=" Task Not Found")
    
    if task.user_id != user.id:
                    raise HTTPException(status_code=401, detail="You are Unauthroize ")

    db.delete(task)
    db.commit()

    return None
