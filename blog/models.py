from django.db import models
from django.utils import timezone
# User model/table and Post model/table will have a relationship
# one to many relationship, User will have multiple posts
from django.contrib.auth.models import User
# to get an url of a specific route
# not using redirect, instead reverse will return a string of the url
from django.urls import reverse

# this is a post model, that is a class of models
# each class is going to be its own table in the database
class Post(models.Model): # Post will inherit from models.Model
    # the atributes title, ..., ... will be own fields in the database
    title = models.CharField(max_length=100)
    content = models.TextField() # just unrestricted text
    # auto_now=True would update the date whenever the post was changed
    # auto_now_add=True would create a date when the post is created but it will not be possible to change that date ever
    date_posted = models.DateTimeField(default=timezone.now)
    # arguments are the ralated table User
    # and how to proceed if a User is deleted > all posts from that User are deleted as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # magig dunder method to return a specified output inside the shell
    def __str__(self):
        return self.title

    # for finding an location/url for any specific instance of a post
    def get_absolute_url(self):
        # will return a full path as a string of the post instance
        return reverse('post-detail', kwargs={'pk': self.pk})
