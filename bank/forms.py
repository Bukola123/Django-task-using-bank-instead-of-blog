from .models import Comment
from django import forms
from django.forms import ModelForm




class CommentForm(ModelForm):
    comment_text =  forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Comment
        fields = ('name', 'comment_text',)

   