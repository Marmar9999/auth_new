from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email = models.CharField(max_length=255 ,unique= True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class User_addional_data(AbstractBaseUser):
    connect = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    disability = models.BooleanField(default=False)
    grade = models.CharField(max_length=50)
    cgpa = models.CharField(max_length=10)

    def __str__(self):
        return self.connect