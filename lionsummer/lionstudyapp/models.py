from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Lionstudyapp(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    image = models.ImageField(null=True, upload_to="images/", blank=True)


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Lionstudyapp, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
