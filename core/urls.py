from django.contrib import admin
from django.urls import path, include
from marketing.views import email_list_signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('email_signup/', email_list_signup, name='email_list_signup'),
]
