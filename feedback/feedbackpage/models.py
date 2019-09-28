from django.db import models

# Create your models here.

class fbcontent(models.Model):
    name = models.TextField(default="anonymous")
    feedback = models.TextField(default="no feedback")
    stdid = models.IntegerField(default=0)
    email = models.TextField(default="noemail")
    pillar = models.TextField(default="nopillar")
    category = models.TextField(default="nocat")