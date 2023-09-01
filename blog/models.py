from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Category(models.Model):
    name=models.CharField( max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='categories'

class News(models.Model):
    
    title=models.CharField(max_length=255)
    content=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=False)
    category=models.ManyToManyField(Category)
    newswriter=models.ForeignKey(User(), on_delete=models.CASCADE,null=True)
    tag=TaggableManager()
    image=models.ImageField(upload_to='blog/',null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='news'
        ordering=['-created_time']
        
        
class Comment(models.Model):
    new=models.ForeignKey(News, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    website=models.CharField(max_length=255)
    Active=models.BooleanField(default=False)
    message=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-created_time']
    
