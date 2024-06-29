from django.db import models

CATEGORY_CHOICES=(
    ('ML', 'Machine Learning'),
    ('DS', 'Data Sciecne'),
    ('And', 'Android')
)

# Create your models here.

class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    URL = models.URLField(max_length=255)
    Short_Intro = models.CharField(max_length=255, db_column='Short Intro')
    Category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    Sub_Category = models.CharField(max_length=255, db_column='Sub-Category')
    Course_Type = models.CharField(max_length=255, db_column='Course Type')
    Language = models.CharField(max_length=255)
    Subtitle_Languages = models.CharField(max_length=255, db_column='Subtitle Languages')
    Skills = models.CharField(max_length=255)
    Instructors = models.CharField(max_length=255)
    Rating = models.CharField(max_length=255)
    Number_of_viewers = models.IntegerField(db_column='Number of viewers')
    Duration = models.CharField(max_length=255)
    Site = models.CharField(max_length=255)
    course_features = models.CharField(max_length=255)
    course_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
