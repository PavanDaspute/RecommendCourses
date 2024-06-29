from pydantic import BaseModel, EmailStr
from typing import Union
from datetime import datetime
from typing import List

class BaseResponse(BaseModel):
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    registered_at: Union[None, datetime] = None
    preferences: str

class Rec_courses(BaseModel):
    id: int
    title : str
    url : str
    category: str

class course_list(BaseModel):
    course_list: List[Rec_courses]

class Course_details(BaseModel):
    id: int 
    title: str
    url: str
    category: str
    description: str

