from django.db import models
from django.core.validators import RegexValidator


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Feedback'

    def __str__(self):
        return self.name


class Pricing(models.Model):
    service_names = models.CharField(max_length=100)
    stage = models.CharField(max_length=10)
    price = models.FloatField()

    class Meta:
        verbose_name_plural = 'Pricing'

    def __str__(self):
        return self.service_names


timeperiod = [
    ('First Choice appointment time', 'First Choice appointment time'),
    ('9 am to 10 am', '9 am to 10 am'),
    ('10:30 am to 11:30 am', '10:30 am to 11:30 am'),
    ('11:30 am to 12:30 pm', '11:30 am to 12:30 pm'),
    ('12:30 am to 1:30 pm', '12:30 am to 1:30 pm'),
    ('1:30 pm to 2:30 pm', '1:30 pm to 2:30 pm'),
    ('2:30 pm to 3:30 pm', '2:30 pm to 3:30 pm'),
    ('3:30 pm to 4:30 pm', '3:30 pm to 4:30 pm'),
    ('4:30 pm to 5:30 pm', '4:30 pm to 5:30 pm'),
]

date = [
    ('Choose Your Date', 'Choose Your Date'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
]


class Appointments(models.Model):

    name = models.CharField(max_length=100)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=
        "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    appointment_time = models.CharField(max_length=50,
                                        choices=timeperiod,
                                        default='1')
    choose_date = models.CharField(max_length=50,
                                   choices=date,
                                   default='Choose Your Date')
    your_message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Appointments'
