from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('tweet',)
        widgets = {
            'tweet': forms.TextInput(attrs={'tweet': 'form-control'}),
        }