from users.models import UserModel, Courses
from fastapi.exceptions import HTTPException
from core.security import get_password_hash
from datetime import datetime
from sklearn.metrics.pairwise import linear_kernel
import pickle
from sqlalchemy.orm import Session
from users.responses import Rec_courses, Course_details
import numpy as np
from users.models import UserModel, Courses
import ast


async def create_user_account(data, db):
    user = db.query(UserModel).filter(UserModel.email == data.email).first()
    if user:
        raise HTTPException(status_code=422, detail="Email is already registered with us.")
    
    new_user = UserModel(
        first_name = data.first_name,
        last_name = data.last_name,
        email = data.email,
        password = get_password_hash(data.password),
        registered_at = datetime.now(),
        preferences = data.preferences
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Function to get recommendations for a user based on their preferences
def get_recommendations(user, n=6, db: Session = None):
    
    user_preferences = [user.preferences]

    print("User Preferences:")
    print(user_preferences)

    recommended_courses = []
    
    # Load the trained model from the pickle file
    with open(r'C:\Users\PAVAN\OneDrive\Desktop\Course_Rec_Project\rec_model\recommendation_model1.pkl', 'rb') as f:
        tfidf, features_matrix = pickle.load(f)

    
    print("User Preferences:", user_preferences)
    user_pref_matrix = tfidf.transform(user_preferences)
    
    # Print shapes for debugging
    print("User Pref Matrix Shape:", user_pref_matrix.shape)
    print("Features Matrix Shape:", features_matrix.shape)
    
    # Compute cosine similarity between user preferences and course features
    sim_scores = linear_kernel(user_pref_matrix, features_matrix)
    
    # Print similarity scores for debugging
    print("Similarity Scores Shape:", sim_scores.shape)
    print("Similarity Scores:", sim_scores)
    
    # Get indices of courses with highest similarity scores
    top_indices = sim_scores.argsort()[0][-n-1:-1][::-1]  # Exclude the user preference itself
    
    # Fetch course data from the database
    courses = db.query(Courses).all()  # Assuming Courses is your SQLAlchemy model

    recommended_courses = [
        {
            'id': courses[idx].course_id,
            'title': courses[idx].Title,
            'url': courses[idx].URL,
            'category': courses[idx].Category
        } for idx in top_indices 
    ]

    # Convert the list of dictionaries to a list of Rec_courses objects
    recommended_courses_models = [Rec_courses(**item) for item in recommended_courses]

    # Wrap the list of Rec_courses objects in a dictionary to match the course_list model structure
    return {"course_list": recommended_courses_models}

def getProductDetails(id, db: Session = None):
    product_details = db.query(Courses).filter(id == Courses.course_id).first()

    if not product_details:
        raise HTTPException(status_code=404, detail="Product not found")

    # Map the query result to the Course_details model
    course_details_response = Course_details(
        id=product_details.course_id,
        title=product_details.Title,
        url=product_details.URL,
        category=product_details.Category,
        description=product_details.Short_Intro
    )

    return course_details_response

def get_courses_by_category(category, n=24, db: Session = None):
    # Fetch courses data from the database by category
    courses = db.query(Courses).filter(Courses.Category == category).limit(n).all()

    if not courses:
        raise HTTPException(status_code=404, detail="No courses found in this category")

    # Map the query result to the Rec_courses model
    recommended_courses = [
        {
            'id': course.course_id,
            'title': course.Title,
            'url': course.URL,
            'category': course.Category
        } for course in courses
    ]

    # Convert the list of dictionaries to a list of Rec_courses objects
    recommended_courses_models = [Rec_courses(**item) for item in recommended_courses]

    # Wrap the list of Rec_courses objects in a dictionary to match the course_list model structure
    return {"course_list": recommended_courses_models}