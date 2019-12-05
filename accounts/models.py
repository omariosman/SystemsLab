from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Salutation(models.Model):
    title =  models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Professor(models.Model):
    salutation         = models.OneToOneField(Salutation, on_delete=models.CASCADE)
    user               = models.OneToOneField(User, on_delete=models.CASCADE)
    bio                = models.TextField(blank=True)
    research_interests = models.TextField(blank=True)
    email              = models.EmailField()
    twitter_profile    = models.URLField(blank=True)
    img                = models.ImageField(upload_to="accounts-images")
