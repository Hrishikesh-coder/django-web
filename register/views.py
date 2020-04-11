from django.shortcuts import render

from . import forms 

def regform(request):

    form = forms.SignUp()

    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'We have received this form again'

        
    
    else :
        html = 'Welcome for the first time'

    return render(request, 'signup.html',{'html': html , 'form':form})
