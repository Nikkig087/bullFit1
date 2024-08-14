from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # Import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Exercise(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    detailed_image = CloudinaryField('detailed_image', blank=True, null=True)  # For larger images
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.user.username}"
