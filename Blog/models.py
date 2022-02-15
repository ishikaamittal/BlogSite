from email.policy import default
from django.utils.timezone import now
from unicodedata import category
from django.db import models
from django.utils import timezone
from PIL import Image
# from users.models import Profile

CATEGORY_CHOICES = [
        ('NEWS', 'News'),
        ('ANDROID', 'Android'),
        ('PC', 'PC'),
        ('GAMING', 'Gaming'),
        ('OTHERS', 'Others'),
    ]

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey("auth.User",
        on_delete = models.CASCADE,
        verbose_name = "written by ")

    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='blog_img')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=now)
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

   