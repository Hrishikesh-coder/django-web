from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Data Flair Django</h1>Hello, you just configured your First URL")

#def data_flair(request):
 #   return redirect()


from django.views.generic.base import RedirectView 
class tutorial(RedirectView): url = 'https://data-flair.training/blogs/category/django/'