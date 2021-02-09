from django.db import models
from datetime import datetime
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    img = models.ImageField(upload_to='posts', null=True, blank=True)
    create_date = models.DateTimeField(default=datetime.now)
    published_date = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('post_detail', kargs={'pk': self.id})

    def publish(self):
        self.published_date = datetime.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(aproved_comment=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    comment_date = models.DateTimeField(default=datetime.now())
    aproved_comment = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('post_list')

    def publish(self):
        self.aproved_comment = True
        self.save()

    def __str__(self):
        return self.text
