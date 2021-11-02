from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # OneToOneField is a link between two models
    image =models.ImageField(default='a.jpg', upload_to = 'profile_pics') # upload_to is the path where the image will be saved

    def __str__(self):
        return f'{self.user.username} Profile'