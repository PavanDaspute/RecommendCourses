from django.contrib import admin
from . models import Courses

# Register your models here.

@admin.register(Courses)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'Title', 'URL', 'Category', 'Rating']