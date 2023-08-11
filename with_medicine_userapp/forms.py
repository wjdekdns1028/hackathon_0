from django.contrib.auth import forms
from .models import CustomUser

#from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'age', 'email', 'image', 'gender', 'phone_unmber']
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()     
        fields = ['username', 'first_name', 'last_name', 'email', 'image', 'gender', 'phone_unmber']