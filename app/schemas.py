from pydantic import BaseModel

"""
Task schemas
"""
class TaskBase(BaseModel):
    name: str
    description: str | None = None
    priority: int

class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class TaskCreate(TaskBase):
    is_done: bool
    
    class Config:
        from_attributes = True


"""
User schemas
"""
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    
    class Config:
        from_attributes = True
