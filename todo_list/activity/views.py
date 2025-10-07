from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def findAll(request):
    return HttpResponse('findAll Method')

@api_view(['POST'])
def create(request):
    return HttpResponse('create method')

@api_view(['PATCH'])
def update(request):
    return HttpResponse('update method')

@api_view(['DELETE'])
def delete(request):
    return HttpResponse('delete method')