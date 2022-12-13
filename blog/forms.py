from django import forms
from django.forms import ModelForm
from .models import CommentDb


class CommentForm(ModelForm):
    class Meta:
        model = CommentDb
        fields = ['comment']
