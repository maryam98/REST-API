from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name

class TodoTask(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(blank=True)
    created=models.DateField(default=timezone.now())
    Category=models.ForeignKey(Category,default='generall',on_delete=models.CASCADE)

    def __str__(self):
        return self.title