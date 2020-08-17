from django.db.models.signals import post_save # a signal of User creatin that will be send to the receiver
from django.contrib.auth.models import User # is the sender of the signal
# a receiver is a function that gets the signal and performs some tasks
from django.dispatch import receiver
from .models import Profile

# when profile is created a default picture will be assigned to the newly created user/profile
# every time a user is created this function will be executed
# to tie the creation of a user to the function execution we need a receiver
# the receiver will be the decorator of the function
@receiver(post_save, sender=User) # when the user is saved than send this signal post_save!, the signal is received by the decorator
def create_profile(sender, instance, created, **kwargs): # the receiver is the create_profile function
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save() # instance is the User
