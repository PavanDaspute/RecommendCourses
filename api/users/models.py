from sqlalchemy import Boolean, Column, Integer, String, DateTime, func, Text
from datetime import datetime

from core.database import Base

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True , autoincrement= True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(255), unique= True, index=True)
    password = Column(String(100))
    registered_at = Column(DateTime, nullable=True)
    preferences = Column(Text)

class Courses(Base):
    __tablename__ = "Courses_data"
    course_id = Column(Integer, primary_key=True)
    Title = Column(String)
    URL = Column(String)
    Short_Intro = Column(String, name= 'Short Intro')
    Category = Column(String)
    Sub_Category = Column(String, name= 'Sub-Category')
    Course_Type = Column(String, name= 'Course Type')
    Language = Column(String)
    Subtitle_Languages = Column(String, name= 'Subtitle Languages') 
    Skills = Column(String)
    Instructors = Column(String)
    Rating = Column(String)
    Number_of_viewers = Column(Integer, name= 'Number of viewers')
    Duration = Column(String)
    Site = Column(String)
    course_features = Column(String)


