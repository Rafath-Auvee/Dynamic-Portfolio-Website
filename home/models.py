from django.db import models
from django.contrib.auth.models import User 


class BlogModel(models.Model):
  title = models.charfield(max_length = 1000)
  content = models.TextField()
  slug = models.SlugField(max_length=1000)
  image = models.ImageField(uploaded_to='blog')
  created_at = models.DateTimeField(auto_now_add=True)
  uploaded_to = models.DateTimeField(auto_now=True)