from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from django.shortcuts import redirect
import numpy as np

def index(request):
    return render(request, 'login/index.html', { 'isWrong': False})

def validate(request):

    email = request.POST['email']
    password = request.POST['pass']

    try:
        person = Person.objects.get(password=password ,email=email)
    except Person.DoesNotExist:
        return render(request, 'login/index.html' ,{ 'isWrong': True})

    url = '/music/'
    key = np.random.randint(500000)
    url = url + str(key) + '/' + str(person.id)

    person.key = str(key)
    person.save()

    return redirect(url)