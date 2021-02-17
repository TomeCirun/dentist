from django import forms
from .models import Feedback, Appointments, timeperiod, date
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'name',
            'name': 'name',
            'id': 'name',
            'placeholder': 'Your Name',
        }),
                           label='')
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'type': 'email',
            'name': 'email',
            'id': 'email',
            'placeholder': 'Your Email',
        }),
                             label='')
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'type': 'content',
            'name': 'content',
            'id': 'content',
            'placeholder': 'Your Message',
        }),
                              label='')

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'content')


class AppointmentsForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'name',
            'name': 'name',
            'id': 'name',
            'placeholder': 'Your Name',
        }),
                           label='')
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=
        "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = forms.CharField(validators=[phone_regex],
                            max_length=15,
                            widget=forms.TextInput(
                                attrs={
                                    'type': 'phone',
                                    'name': 'phone',
                                    'id': 'phone',
                                    'placeholder': 'Your Phone',
                                }),
                            label='')

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'type': 'email',
            'name': 'email',
            'id': 'email',
            'placeholder': 'Your Email',
        }),
                             label='')
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'address',
            'name': 'adress',
            'id': 'adress',
            'placeholder': 'Your Address',
        }),
                              label='')
    appointment_time = forms.ChoiceField(choices=timeperiod,
                                         widget=forms.Select(
                                             attrs={
                                                 'type': 'appointment_time',
                                                 'name': 'appointment_time',
                                                 'id': 'appointment_time',
                                             }),
                                         label='')
    choose_date = forms.ChoiceField(
        choices=date,
        widget=forms.Select(attrs={
            'type': 'choose_date',
            'name': 'choose_date',
            'id': 'choose_date',
        }),
        label='')
    your_message = forms.CharField(widget=forms.Textarea(
        attrs={
            'type': 'your_message',
            'name': 'your_message',
            'id': 'your_message',
            'placeholder': 'Your Message',
        }),
                                   label='')

    class Meta:
        model = Appointments
        fields = ('name', 'phone', 'email', 'address', 'appointment_time',
                  'choose_date', 'your_message')