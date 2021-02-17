# Generated by Django 3.1.4 on 2021-01-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20201229_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='appointment_time',
            field=models.CharField(choices=[('1', 'First Choice appointment time'), ('2', '9 am to 10 am'), ('3', '10:30 am to 11:30 am'), ('4', '11:30 am to 12:30 pm'), ('5', '12:30 am to 1:30 pm'), ('6', '1:30 pm to 2:30 pm'), ('7', '2:30 pm to 3:30 pm'), ('8', '3:30 pm to 4:30 pm'), ('9', '4:30 pm to 5:30 pm')], default=1, max_length=20),
        ),
    ]
