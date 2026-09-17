from pydantic import BaseModel

class UserSchema(BaseModel):
    name :str
    username : str
    password : str
    email : str
class UpdateSchema(BaseModel):
    name :str | None = None
    password : str | None = None
    email : str | None = None
    
class UserResponseSchema(BaseModel):
    id:int
    name :str
    username : str
    email : str
    
    
class LoginSchema(BaseModel):
    username : str
    password : str

