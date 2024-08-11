from django import forms
from .models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django_summernote.widgets import SummernoteWidget

from .models import Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['title', 'description', 'image']
        widgets = {
            'description': SummernoteWidget(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
