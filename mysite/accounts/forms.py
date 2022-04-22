from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Order 


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields ='__all__' #create model with all field (assign a list to choose specific fields)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']