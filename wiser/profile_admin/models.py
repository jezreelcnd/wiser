from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):  #to return title when adding a post
    return self.title
  class Meta:  #to avoid plural of the model Postss
    verbose_name_plural = "Posts"

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)  #unique
    message = models.CharField(max_length=500, blank=True)  #optional
    #owner = models.ForeignKey(
    #    User, related_name="leads", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)