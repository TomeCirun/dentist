# Generated by Django 3.1.4 on 2020-12-29 09:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_appointments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointments',
            options={'verbose_name_plural': 'Appointments'},
        ),
        migrations.AlterField(
            model_name='appointments',
            name='phone',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
