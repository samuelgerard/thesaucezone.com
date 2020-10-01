#Database content templates
import random
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    title = models.CharField(max_length = 100) #title w/ character field with max 100
    content = models.TextField() #unrestricted field of text
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if a user is deleted, delete all their post
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk}) #returns the full path as a string

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, default=random.randint(1,10000))
    body = models.TextField(max_length=160, default="Comment Here")
    created_on = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name) #what is seen in the admin interface
        
