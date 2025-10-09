from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.serializers import serialize
from . import service
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def findAll(request):
    activities = service.findAll()
    activities_json = serialize('json', activities)
    return HttpResponse(activities_json, content_type='application/json')

@api_view(['POST'])
def create(request):
    author = request.data['author']
    name = request.data['name']
    date = request.data['date']
    description = request.data['description']
    city = request.data['city']
    service.create(author, name, date, description, city)
    return HttpResponse(True, content_type='application/json')

@api_view(['PATCH'])
def update(request):
    name = request.data['name']
    new_name = request.data['new_name']
    new_date = request.data.get('new_date')
    new_description = request.data.get('new_description')
    new_city = request.data.get('new_city')
    service.update(name, new_name, new_date, new_description, new_city)
    return HttpResponse(True, content_type='application/json')

@api_view(['DELETE'])
def delete(request):
    name = request.data['name']
    service.delete(name)
    return HttpResponse('delete method')