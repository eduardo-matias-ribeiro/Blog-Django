from django import forms
from django.forms import ModelForm, Textarea
from .models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
