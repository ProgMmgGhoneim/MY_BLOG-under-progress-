from django import forms
from blog_app.models import *


class PostForm(forms.ModelForm):

    class Meta:
        models =Post
        fields = ('author','title','text')

        widgets ={
        'title':forms.TextInput(attrs={'class': 'title'}),
        'text':forms.Textarea(attrs={"class":'text'})
        }
class CommentForm(forms.ModelForm):

    class Meta:
        models =Comments
        fielde= ('author','text')
        widgets ={
        'author':forms.TextInput(attrs={'class': 'title'}),
        'text':forms.Textarea(attrs={"class":'text'})
        }
