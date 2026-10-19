from django.http import HttpResponse
from django.shortcuts import render
from .models import Student,Course

def home(request):
    students = Student.objects.all()
    courses = Course.objects.all()

    return render(request, 'core/home.html', {
        'students': students,
        'courses': courses
    })

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request,'core/contact.html')
