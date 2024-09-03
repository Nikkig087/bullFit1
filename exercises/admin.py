from django.contrib import admin
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Exercise, Comment, ContactMessage, CommentReport
from cloudinary import CloudinaryImage
from django.utils.html import format_html


class ExerciseAdminForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = "__all__"
        widgets = {
            "description1": SummernoteWidget(),
            "detailed_description1": SummernoteWidget(),
            "detailed_description2": SummernoteWidget(),
        }


# Define the custom form to use Summernote for the body field in Comment


class CommentAdminForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        widgets = {
            "body": SummernoteWidget(),  # Use Summernote for the body field
        }


# Customize the ExerciseAdmin to use the custom form


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    form = ExerciseAdminForm  # Use the custom form with Summernote
    list_display = (
        "title",
        "description",
        "detailed_description1",
        "detailed_description2",
        "created_at",
        "image_tag",
    )
    search_fields = (
        "title",
        "description",
        "detailed_description1",
        "detailed_description2",
    )
    list_filter = ("created_at",)

    def image_tag(self, obj):
        if obj.image:
            # Use the 'url' attribute to get the image's URL
            webp_url = CloudinaryImage(obj.image.public_id).build_url(format="webp")
            return format_html('<img src="{}" width="100" height="100" />', webp_url)
        return "No image"
    image_tag.short_description = 'Image'


# Customize the CommentAdmin to use the custom form


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm  # Use the custom form with Summernote
    list_display = ("exercise", "user", "created_on", "approved")
    search_fields = ("exercise__title", "user__username", "body")
    list_filter = (
        "approved",
        "created_on",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message", "created_at")
    search_fields = ("name", "email", "message")
    list_filter = ("name", "created_at")


@admin.register(CommentReport)
class CommentReportAdmin(admin.ModelAdmin):
    readonly_fields = ("user", "comment", "reason", "created_at")
    list_display = ("user", "comment", "reason", "created_at")
    list_filter = ("created_at", "user")
    search_fields = ("user__username", "comment__body", "reason")
