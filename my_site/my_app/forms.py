from django import forms
from .models import Review
from django.forms import ModelForm, Textarea

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'review' : Textarea(),
        }