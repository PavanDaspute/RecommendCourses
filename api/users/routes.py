from fastapi import APIRouter, status, Depends, Request
from sqlalchemy.orm import Session
from core.database import get_db
from users.schemas import CreateUserRequest
from users.services import create_user_account
from fastapi.responses import JSONResponse
from users.models import UserModel
from core.security import oauth2_scheme
from users.responses import UserResponse, Rec_courses, course_list, Course_details
from users.services import get_recommendations, getProductDetails, get_courses_by_category




router = APIRouter(
    prefix = "/users",
    tags = ["Users"],
    responses={404: {"description": "Not Found"}}
)

user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"Description": "Not Found"}},
    dependencies=[Depends(oauth2_scheme)]
)

@router.post('', status_code= status.HTTP_201_CREATED)
async def create_user(data: CreateUserRequest, db: Session = Depends(get_db)):
    await create_user_account(data = data, db=db)
    payload = {"message":"User account has been successfully created."}
    return JSONResponse(content = payload)

@user_router.post('/me', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def get_user_detail(request: Request):
    return request.user

@user_router.post('/me/recommendations', status_code=status.HTTP_201_CREATED, response_model= course_list)
def get_user_recommendations(user: UserResponse = Depends(get_user_detail), db: Session = Depends(get_db)):
    return get_recommendations(user, 6, db)

@user_router.get('/productsDetails/{course_id}', status_code=status.HTTP_201_CREATED, response_model= Course_details)
def get_course_details(course_id: int, db: Session = Depends(get_db)):
    return getProductDetails(course_id, db)

@user_router.get('/courseCategory/{category}', status_code=status.HTTP_201_CREATED, response_model= course_list)
def get_course_details(category: str, db: Session = Depends(get_db)):
    return get_courses_by_category(category,24, db)


