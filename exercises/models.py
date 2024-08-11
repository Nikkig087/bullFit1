from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField  # Import CloudinaryField

class Exercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)  # Use CloudinaryField for image storage

    def __str__(self):
        return self.title

class Comment(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.text[:20]}'
