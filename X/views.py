from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Id(request, id=1):
    return HttpResponse(f'Hello, {id}')

def name(request, name='elon'):
    return HttpResponse(f'Your name: {name}')

def name2(request, name = 'unknown'):
    return HttpResponse(name)

def age(request, age = None):
    return HttpResponse(f"Your age: {age}")