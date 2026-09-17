from pydantic import BaseModel

class UserSchema(BaseModel):
    name :str
    username : str
    password : str
    email : str
    
class UserResponseSchema(BaseModel):
    id:int
    name :str
    username : str
    email : str
    
    
class LoginSchema(BaseModel):
    username : str
    password : str
    