# Create your models here.
#table ,columns
from django.db import models

# Create your models here.
class Task(models.Model):
    task=models.CharField(max_length=255)
    is_completed=models.BooleanField(default=False)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)