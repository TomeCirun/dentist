from django.contrib import admin
from .models import Feedback, Pricing, Appointments


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'content', 'date')
    date_hierarchy = 'date'


class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address', 'appointment_time',
                    'choose_date', 'your_message')


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Pricing)
admin.site.register(Appointments, AppointmentsAdmin)
