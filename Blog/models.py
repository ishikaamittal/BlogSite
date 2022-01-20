from unicodedata import category
from django.db import models
from django.utils import timezone

# Create your models here.
class PostBlog(models.Model):
    category = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)