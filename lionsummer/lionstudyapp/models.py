from django.db import models


# Create your models here.
class Lionstudyapp(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
