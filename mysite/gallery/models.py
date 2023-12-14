from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.CharField(max_length=100, blank=True, null=True, 
        help_text='Comma-separated list of tags')

    def __str__(self):
        return self.description
    
    def get_tags_list(self):
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []