# Generated by Django 4.2.13 on 2024-06-05 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('URL', models.URLField(max_length=255)),
                ('Short_Intro', models.CharField(db_column='Short Intro', max_length=255)),
                ('Category', models.CharField(choices=[('ML', 'Machine Learning'), ('DS', 'Data Sciecne'), ('And', 'Android')], max_length=3)),
                ('Sub_Category', models.CharField(db_column='Sub-Category', max_length=255)),
                ('Course_Type', models.CharField(db_column='Course Type', max_length=255)),
                ('Language', models.CharField(max_length=255)),
                ('Subtitle_Languages', models.CharField(db_column='Subtitle Languages', max_length=255)),
                ('Skills', models.CharField(max_length=255)),
                ('Instructors', models.CharField(max_length=255)),
                ('Rating', models.CharField(max_length=255)),
                ('Number_of_viewers', models.IntegerField(db_column='Number of viewers')),
                ('Duration', models.CharField(max_length=255)),
                ('Site', models.CharField(max_length=255)),
                ('course_features', models.CharField(max_length=255)),
                ('course_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
