from django import forms
from .models import Students

class Studentform(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
