import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, "app/home.html")

def course_details(request, course_id):
    context = {
        'course_id': course_id,
    }
    return render(request, 'app/CoursePage.html', context)

def category_page(request, category):
    context = {
        'category': category,
    }
    return render(request, 'app/Category.html', context)


def view_user(request):
    return render(request, 'app/UserProfile.html')

def AboutUs(request):
    return render(request, 'app/AboutUs.html')

def ContactUs(request):
    return render(request, 'app/ContactUs.html')

@csrf_exempt
def user_details_view(request):
    token = request.headers.get('Authorization').split()[1]
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user = User.objects.get(id=payload['user_id'])
        user_details = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return JsonResponse(user_details)
    except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist):
        return JsonResponse({'detail': 'Invalid token or user not found'}, status=401)
    
 # Constants
JWT_EXP_DELTA_SECONDS = 3600  # Adjust as needed
JWT_SECRET = 'your_jwt_secret'
JWT_ALGORITHM = 'HS256'

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = email  # Assuming username is the same as email
        password = request.POST['password']
        preferences = request.POST.get('preferences', '')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'User already exists'}, status=400)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Assuming you have a Profile model for storing additional user data like preferences
        # If not, you can skip this part or adapt it to your own model
        # Profile.objects.create(user=user, preferences=preferences)

        payload = {
            'user_id': user.id,
            'username': user.username,
            'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
        }
        jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
        response = JsonResponse({'token': jwt_token})
        response.set_cookie('jwt', jwt_token, httponly=True)  # Store JWT in cookie
        return response
    else:
        return render(request, 'app/registration.html')
    
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            payload = {
                'user_id': user.id,
                'username': user.username,
                'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
            }
            jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
            response = JsonResponse({'token': jwt_token})
            response.set_cookie('jwt', jwt_token, httponly=True)  # Store JWT in cookie
            return response
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=400)
    else:
        return render(request, 'app/login.html')

@csrf_exempt
def user_details_view(request):
    token = request.headers.get('Authorization').split()[1]
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user = User.objects.get(id=payload['user_id'])
        user_details = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return JsonResponse(user_details)
    except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist):
        return JsonResponse({'detail': 'Invalid token or user not found'}, status=401)
    

def logout_view(request):
    response = redirect('/login')  # Redirect to login page after logout
    response.delete_cookie('jwt')  # Delete the JWT cookie
    return response