from sqlalchemy import Column , Integer,String,Boolean
from src.utils.db import Base


class TaskModel(Base):
    __tablename__ = "user_task"
    
    id = Column(Integer,primary_key=True)
    title = Column(String)
    description = Column(String)
    is_complete = Column(Boolean,default = False)