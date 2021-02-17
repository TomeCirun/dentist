from django import forms
from django.db.models import fields
from django.forms.models import model_to_dict
from .models import Signup


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'type': 'email',
            'name': 'email',
            'id': 'email',
            'placeholder': 'Type your email address',
        }),
        label='')

    class Meta:
        model = Signup
        fields = ('email', )
