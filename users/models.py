from django.db import models
from django.contrib.auth.models import User
from PIL import Image #Pillow library for image handling like profile pictures

#REMEMBER, YOU NEED TO RUN MIGRATIONS FOR ANY MODELS TO TAKE EFFECT
#MAKEMIGRATIONS -> MIGRATE
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #for profile picture

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) 



# Create your models here.
