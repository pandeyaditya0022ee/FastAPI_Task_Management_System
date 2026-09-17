from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException
from sqlalchemy import select


def create_task(body : TaskSchema, db : Session):
    data = body.model_dump()
    new_task = TaskModel(title = data["title"], description= data["description"], is_complete = data["is_complete"])
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    
    return {"message" : "Task created sucessfully.....", "data" : new_task}


def get_tasks(db : Session):
    tasks = db.query(TaskModel).all()
    return {"message" : "All Tasks....", "data" : tasks}


def get_specific_task(task_id : int , db : Session):
    task = db.query(TaskModel).get(task_id)  
    if not task:
        raise HTTPException(status_code= 404, detail= " Task Not Found")
    
    return {"message" : "Task Fetch Sucessfully...", "data" : task}


def update_task(body:TaskSchema,task_id : int,db : Session):
    task = db.query(TaskModel).get(task_id)
        
    if not task:
        raise HTTPException(status_code= 404, detail= " Task Not Found")
    
    # task.title = body.title
    # task.description = body.description
    # task.is_complete = body.is_complete
    
    body = body.model_dump(exclude_unset=True)
    
    for key, value in body.items():
        setattr(task , key , value)
    
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return {"message" : "Task Update Sucessfully....","data" : task}

def delete_task(task_id : int, db :Session):
    task = db.query(TaskModel).get(task_id)
            
    if not task:
        raise HTTPException(status_code= 404, detail= " Task Not Found")

    db.delete(task)
    db.commit()
    
    return None

