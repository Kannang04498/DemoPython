from . models import Task
from django import forms
class Todoform(forms.ModelForm):
    class Meta:
        model=Task
        #fields to be changed in future
        fields=['name','priority','date']