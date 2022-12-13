from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class PostDb(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class CommentDb(models.Model):
    post = models.ForeignKey(PostDb, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment on {self.post} by {self.name}"

    def get_absolute_url(self):
        return reverse_lazy('create-comment', kwargs={'pk': self.pk})