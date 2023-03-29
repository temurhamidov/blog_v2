from django import forms
from django.core.exceptions import ValidationError

from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'category',
            'image',
            'text',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) <= 10:
            raise ValidationError('Title 10 ta belgidan kam bulmasligi kerak ! ')
        return title


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
            'rating',
        ]


