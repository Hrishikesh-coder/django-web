from django.shortcuts import render
from . import forms
from django.core.mail import send_mail
from Test.settings import EMAIL_HOST_USER

def subscribe(request):
    sub = forms.Subscribe()

    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Hello!!'
        message = 'How are you?'
        recepient = str(sub['Email'].value())
        send_mail(subject,message,EMAIL_HOST_USER, [recepient] ,fail_silently=False)

        return render(request,'subscribe/success.html',{'recepient':recepient})

    return render(request,'subscribe/index.html',{'form':sub})
