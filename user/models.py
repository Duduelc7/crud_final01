from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class Film(models.Model):
    name= models.CharField(max_length=255, unique=True )
    users = models.ManyToManyField(User, related_name='films') # user.films.all()