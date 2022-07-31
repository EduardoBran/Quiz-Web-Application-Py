from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *


class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
        

class addQuestionForm(ModelForm):
    class Meta:
        model = QuestionsModel
        fields = "__all__"
