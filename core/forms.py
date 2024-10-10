from django import forms
from .models import FileEncryption
from django.forms import ModelForm

class FileUpload(forms.ModelForm):
    class Meta:
        model = FileEncryption
        fields = ['file_name', 'uploade_file']  

        widgets = {
            'file_name': forms.TextInput(attrs={'class': 'pw-box', 'placeholder': 'file name'}),  
            'uploade_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),  
            
        }
