from django.db import models

# Create your models here.
class Wordgame(models.Model):
    word = models.CharField(max_length=100)
    
