from django.db import models
from django.contrib.auth.models import User
from PIL import Image # import the Image module from the pillow library


class Profile(models.Model):
    # organizing one to one realationship and bavavior when the user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # self is the instance of the profile with the users information etc.
    def __str__(self):
        return f'{self.user.username} Profile'

    # changing image size
    # **kwargs added ... WHY?
    # *args are positional arguments
    # **kwargs are key word arguments
    # def save(self, *args, **kwargs):
        # super is the parent class here
        # saving the instace
        # super().save(*args, **kwargs)

        # img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
            # output_size = (300, 300) # tuple
            # img.thumbnail(output_size)
