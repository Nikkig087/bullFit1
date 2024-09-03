from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # Import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Exercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    detailed_description1 = models.TextField(default="description1")
    detailed_description2 = models.TextField(default="description2")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    image = CloudinaryField("image", blank=True, null=True)
    top_row_image = CloudinaryField("top_row_image", blank=True, null=True)
    bottom_row_image = CloudinaryField(
        "bottom_row_image", blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    exercise = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.user.username}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} at {self.created_at}"


class CommentReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
