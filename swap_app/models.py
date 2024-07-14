from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string

class all_items(models.Model):
    product_type = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    color = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=50)
    picture = models.ImageField(blank=True)
    slug = models.SlugField(default=get_random_string(length=20))
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.product_type


class users(models.Model):
    birthday = models.DateTimeField(max_length=255)
    country = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(default="https://bootdey.com/img/Content/avatar/avatar7.png")
    username = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username
