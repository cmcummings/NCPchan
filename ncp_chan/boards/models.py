from django.db import models
from django.utils import timezone

class Thread(models.Model):
    board = models.CharField(max_length=5)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    # TODO add images

class Reply(models.Model):
    author = models.CharField(max_length=20)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    # TODO add images
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)