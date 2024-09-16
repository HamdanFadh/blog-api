from django.db import models

# Create your models here.

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=False, default='')
    body = models.TextField(blank=True, default='')
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    author = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'