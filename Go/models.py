from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type_choices = [
        ('teacher', 'Преподаватель'),
        ('student', 'Студент')
    ]
    user_type = models.CharField(max_length=100, choices=user_type_choices)

class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
