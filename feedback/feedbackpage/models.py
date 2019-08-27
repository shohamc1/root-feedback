from django.db import models

# Create your models here.

class fbcontent(models.Model):
    stdname = models.TextField()
    feedback = models.TextField()