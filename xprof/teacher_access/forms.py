from django import forms
from .models import Teacher


class AuthForm(forms.Form):
    login = forms.CharField(max_length=100, help_text="Enter your id")
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, help_text="Enter password")


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
