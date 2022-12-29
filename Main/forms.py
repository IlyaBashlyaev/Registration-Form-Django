from .models import Account
from django.forms import ModelForm, TextInput

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password']

        widgets = {
            'username': TextInput(attrs = {
                'class': 'inner-form-input username',
                'placeholder': 'Enter Username:',
                'onclick': 'wrongClick(0)'
            }),

            'email': TextInput(attrs = {
                'class': 'inner-form-input email',
                'placeholder': 'Enter Email:',
                'onclick': 'wrongClick(1)'
            }),

            'password': TextInput(attrs = {
                'type': 'password',
                'class': 'inner-form-input password',
                'placeholder': 'Enter Password:',
                'onclick': 'wrongClick(2)'
            })
        }