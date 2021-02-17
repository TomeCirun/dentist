from django.shortcuts import render
from django.core.mail import send_mail
from marketing.views import EmailSignupForm
from .forms import AppointmentsForm, FeedbackForm


from .models import Pricing


def home(request):

    if request.method == 'POST':
        a = AppointmentsForm(request.POST)
        if a.is_valid():
            a.save()
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            address = request.POST.get('address')
            appointment_time = request.POST.get('appointment_time')
            date = request.POST.get('choose_date')
            your_message = request.POST.get('your_message')

            return render(
                request, 'website/home.html', {
                    'a': a,
                    'name': name,
                    'phone': phone,
                    'email': email,
                    'address': address,
                    'appointment_time': appointment_time,
                    'date': date,
                    'your_message': your_message
                })

    a = AppointmentsForm()
    form = EmailSignupForm()
    context = {'form': form, 'a': a}
    return render(request, 'website/home.html', context)


def about(request):
    form = EmailSignupForm()
    context = {'form': form}
    return render(request, 'website/about.html', context)


def web_service(request):
    form = EmailSignupForm()
    context = {'form': form}
    return render(request, 'website/service.html', context)


def pricing(request):
    form = EmailSignupForm()
    pricing = Pricing.objects.all()
    context = {'form': form, 'pricing': pricing}
    return render(request, 'website/pricing.html', context)


def contact(request):
    form = EmailSignupForm()
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        name = request.POST.get('name')
        if f.is_valid():
            f.save()

            # send an email
            send_mail(
                'Admin Feedback',  # subject
                'Proveri Admin Feedback',  # the message
                'cirun@live.com',  # from email
                ['cirunce@gmail.com'],  # to email
            )
            return render(request, 'website/contact.html', {'name': name})

    else:
        f = FeedbackForm()
        context = {'form': form, 'f': f}
        return render(request, 'website/contact.html', context)
