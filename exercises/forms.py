from django import forms
from .models import Comment, ContactMessage

# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from allauth.account.forms import SignupForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]  # Ensure 'author' is not included here


class CustomSignupForm(SignupForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("This field is required.")
        return email


class ReportCommentForm(forms.Form):
    comment_text = forms.CharField(
        widget=forms.Textarea(attrs={"readonly": "readonly"})
    )
    reason = forms.CharField(
        widget=forms.Textarea, label="Reason for Reporting"
    )
