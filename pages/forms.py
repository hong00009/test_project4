from django import forms
from .models import Page, Comment

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('page',)
        widgets = {
            'choice' : forms.RadioSelect()
        }
