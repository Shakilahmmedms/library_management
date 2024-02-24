from django import forms
from .models import BookPosts,Comment

class bookForm(forms.ModelForm):
    class Meta:
        model = BookPosts
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']