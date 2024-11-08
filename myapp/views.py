from django.shortcuts import render
from .models import Student

# Create your views here.
def home(h):
    s = Student.objects.all()
    return render(h, 'index.html' , {'s':s})