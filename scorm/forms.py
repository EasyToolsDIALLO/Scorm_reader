# forms.py
from django import forms
from .models import MyScormModel


class MyScormForm(forms.ModelForm):
    class Meta:
        model = MyScormModel
        fields = ['file']
