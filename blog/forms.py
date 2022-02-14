from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        maodel = Comment
        fields = ('body',)
