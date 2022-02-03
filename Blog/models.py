from email.policy import default
from django.utils.timezone import now
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# from users.models import Profile

CATEGORY_CHOICES = [
        ('NEWS', 'News'),
        ('ANDROID', 'Android'),
        ('PC', 'PC'),
        ('GAMING', 'Gaming'),
        ('OTHERS', 'Others'),
    ]

# Create your models here.
class PostBlog(models.Model):
    author = models.ForeignKey("auth.User",
        on_delete = models.CASCADE,
        verbose_name = "written by ")

    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
        
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

   