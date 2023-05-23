from datetime import datetime
from django.db import models
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=5000)
    author = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000)
    comments_author = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)


