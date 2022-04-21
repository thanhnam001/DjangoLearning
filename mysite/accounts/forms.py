from django.forms import ModelForm
from .models import Order 


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields ='__all__' #create model with all field (assign a list to choose specific fields)