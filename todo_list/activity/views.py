from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def findAll(request):
    return HttpResponse('findAll Method')

def create(request):
    return HttpResponse('read method')

def update(request):
    return HttpResponse('update method')

def delete(request):
    return HttpResponse('delete method')