from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['numar_matricol', 'prenume',
                  'nume', 'email', 'specializarea', 'media']
        labels = {
            'numar_matricol': 'Numar matricol',
            'prenume': 'Prenume',
            'nume': 'Nume',
            'email': 'Email',
            'specializarea': 'Specializarea',
            'media': 'Media'
        }
        widgets = {
            'numar_matricol': forms.NumberInput(attrs={'class': 'form-control'}),
            'prenume': forms.TextInput(attrs={'class': 'form-control'}),
            'nume': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'specializarea': forms.TextInput(attrs={'class': 'form-control'}),
            'media': forms.NumberInput(attrs={'class': 'form-control'}),
        }
