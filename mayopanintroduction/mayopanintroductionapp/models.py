from django.db import models

# Create your models here.
class ExplanationModel(models.Model):
    date = models.DateField()
    text = models.TextField()