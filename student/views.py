from django.shortcuts import render
from .models import Student
from django.http import HttpResponse 

def student_show(request):
    student = Student.objects.order_by('roll_no')
    return render(request, 'student_show.html',{'student': student})

