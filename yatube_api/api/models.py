from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=64)
    slug = models.CharField(max_length=16)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Post(models.Model):
    text = models.CharField(max_length=256)
    author = models.ForeignKey(
        User, related_name='post', on_delete=models.CASCADE)
    image = models.ImageField()
    group = models.ForeignKey(
        Group, related_name='posts', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(
        User, related_name='comment', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
