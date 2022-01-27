from email.policy import default
from django.utils.timezone import now
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid

# Create your models here.
class PostBlog(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=now)
    # slug = models.SlugField(default=uuid.uuid1) # new


    def __str__(self):
        return self.title

   