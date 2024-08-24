from django.contrib import admin
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Exercise, Comment

# Define the custom form to use Summernote for the description field in Exercise
class ExerciseAdminForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'
        widgets = {
            'description1': SummernoteWidget(),  # Use Summernote for the description field
            'detailed_description1': SummernoteWidget(),  # Use Summernote for the description field
            'detailed_description2': SummernoteWidget(),  # Use Summernote for the description field
        }

# Define the custom form to use Summernote for the body field in Comment
class CommentAdminForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'body': SummernoteWidget(),  # Use Summernote for the body field
        }

# Customize the ExerciseAdmin to use the custom form
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    form = ExerciseAdminForm  # Use the custom form with Summernote
    list_display = ('title','description', 'detailed_description1','detailed_description2', 'created_at', 'image')
    search_fields = ('title', 'description', 'detailed_description1','detailed_description2')
    list_filter = ('created_at',)

# Customize the CommentAdmin to use the custom form
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm  # Use the custom form with Summernote
    list_display = ('exercise', 'user', 'created_on', 'approved')
    search_fields = ('exercise__title', 'user__username', 'body')
    list_filter = ('approved', 'created_on')

