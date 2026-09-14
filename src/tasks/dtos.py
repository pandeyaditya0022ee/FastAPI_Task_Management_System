from pydantic import BaseModel



class TaskSchema(BaseModel):
    title : str
    description : str 
    is_complete : bool = False