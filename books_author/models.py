from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    auther = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    title = models.CharField(max_length=100) 
    description = models.TextField(max_length=800)
    rating = models.IntegerField()
    publish_date = models.DateField()

    def __str__(self):
        return self.title