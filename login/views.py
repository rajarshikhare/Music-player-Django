from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from django.shortcuts import redirect

def index(request):
    return render(request, 'login/index.html', { 'isWrong': False})

def validate(request):

    email = request.POST['email']
    password = request.POST['pass']

    try:
        person = Person.objects.get(password=password ,email=email)
    except Person.DoesNotExist:
        return render(request, 'login/index.html' ,{ 'isWrong': True})


    return redirect('http://127.0.0.1:8000/music/', {test: 'dhf'})