from django.forms import ModelForm
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.models import User
from .models import DeliveryzeUser

placeholders = {
  'username':'Username',
  'password':'Password',
  'email':'Email',
  'first_name': 'First Name',
  'last_name': 'Last Name',
  'address':'Address in Chicago', 
  'zipCode':'ZIP Code',
  'phoneNumber':'Phone Number'}

class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ['email','password','first_name','last_name']
    widgets = {k: TextInput(attrs={'class':'span3','placeholder':placeholders[k]}) for k in fields}
    widgets['password'] = PasswordInput(attrs={'class':'span3','placeholder':'Password'})
    

class DeliveryzeUserForm(ModelForm):
  class Meta:
    model = DeliveryzeUser
    fields = ['address','zipCode','phoneNumber']    
    widgets = {k: TextInput(attrs={'class':'span3','placeholder':placeholders[k]}) for k in fields}
    #labels = { k:'' for k in fields}
    #error_messages = { k:{'required':''} for k in fields}
    #help_texts = { k:'' for k in fields}
