from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email = models.CharField(max_length=255 ,unique= True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.email

class UserActivity(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=10, choices=(('login', 'Login'), ('logout', 'Logout')))

    def __str__(self):
        return f"{self.email} - {self.action} at {self.timestamp}"