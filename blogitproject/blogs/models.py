from django.contrib.postgres.fields import ArrayField
from django.db import models
from profiles.models import Profile
from comments.models import Comment
from taggit.managers import TaggableManager
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250, blank=False, default='Without title')
    text = models.TextField(default='', blank=False)
    text_slug = models.CharField(max_length=200, default='', blank=True)
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='blog_image/%Y/%m/%d', verbose_name='Blog Image', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField(Comment, blank=True)
    likes = ArrayField(models.IntegerField(), blank=True, default=list, help_text='Collects profile ids as Integer')
    is_published = models.BooleanField(default=True, blank=True)
    tags = TaggableManager(blank=True, verbose_name='Теги')
    
    def save(self, *args, **kwargs):
        self.text_slug = self.text[:197] + '...' 
        super(Blog, self).save(*args, **kwargs)