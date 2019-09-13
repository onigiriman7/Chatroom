from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

def send_email(request):
    subject = 'Thank you for registering to our site'
    message = 'Yo Bebe, lick my ass. '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['gamerholes@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect(reverse('chat:index'))
