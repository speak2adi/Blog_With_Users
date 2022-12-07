from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profle_pics')

    def __str__(self):
        return f"{self.user.username}'s profile"

    # overiding the save method to allow for resizing images
    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        # checking the size of the image and reshape to save at the same image path
        if img.width > 300 and img.height > 300:
            resize_by = (300, 300)
            img.thumbnail(resize_by)
            img.save(self.image.path)
