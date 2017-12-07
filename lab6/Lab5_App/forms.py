from django import  forms
from .models import *

class Testforms(forms.ModelForm):
    class Meta:
        model = Test
        exclude = [""]

class Userforms(forms.ModelForm):
    class Meta:
        model = User
        exclude = [""]