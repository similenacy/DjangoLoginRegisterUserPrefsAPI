from django.db import models
from django.contrib.auth.models import User

# Create your models here.\



class User_Preference(models.Model):
    user = models.OneToOneField('auth.User', related_name='preferences', primary_key=True, on_delete=models.CASCADE)
    color = models.CharField(max_length=100, blank=True)
    music = models.CharField(max_length=100, blank=True)
    food = models.CharField(max_length=100, blank=True)
    drink = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['user']


    