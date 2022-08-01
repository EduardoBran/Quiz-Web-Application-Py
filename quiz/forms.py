import imp

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.forms.fields import EmailField
from django.forms.forms import Form

from .models import *


class createUserForm(UserCreationForm):
    username = forms.CharField(label='Usuário', min_length=5, max_length=150)
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)  
    
    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        
        if new.count():
            raise ValidationError("User Already Exist")
        return username
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("As senhas estão diferente.")  
        return password2  
    
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password']
        )
        return user

# class createUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username']
        

class addQuestionForm(ModelForm):
    class Meta:
        model = QuestionsModel
        fields = "__all__"
