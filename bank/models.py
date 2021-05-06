from django.db import models

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.timezone import now




class Post(models.Model):

    title = models.CharField(max_length=200)

    author = models.ForeignKey(

        'auth.User', on_delete=models.CASCADE
    )

    body = models.TextField()
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= 'comments')
    comment_text = models.CharField(max_length=140)
    name = models.ForeignKey('auth.user', on_delete=models.CASCADE,)

    def __str__(self):
        return f'comment by: {self.name}'
