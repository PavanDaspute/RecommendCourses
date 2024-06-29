from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path('login/', views.login_view, name='login'),
    path('auth/user', views.user_details_view, name='user_details'),
    path('CoursePage/<int:course_id>/', views.course_details, name='CoursePage'),
    path('CategoryPage/<str:category>/', views.category_page, name='CategoryPage'),
    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path('ContactUs/', views.ContactUs, name='ContactUs'),
    path('UserProfile/', views.view_user, name='UserProfile'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.register_view, name='registration')
    
]