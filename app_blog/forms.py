# -*- coding: utf-8 -*-
from django import forms
from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    image = forms.FileField(
        widget=forms.ClearableFileInput(),
        required=False
    )

    class Meta:
        model = ArticleImage
        fields = '__all__'