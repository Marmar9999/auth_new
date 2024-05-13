from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email = models.CharField(max_length=255 ,unique= True)
    password = models.CharField(max_length=255)
    


    def __str__(self):
        return self.email

class activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)  # Describes the user action
    timestamp = models.DateTimeField(auto_now_add=True)  # Records activity time

    def __str__(self):
        return f"{self.user.email} - {self.action} ({self.timestamp})"
    