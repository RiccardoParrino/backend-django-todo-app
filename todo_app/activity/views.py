from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Activity
from django.core import serializers

# Create your views here.
class ActivityView(View):
    def get (self, request, *args, **kwargs):
        data = serializers.serialize("json", Activity.objects.all())
        return HttpResponse(data)

    def post (self, request, *args, **kwargs):
        author = request.data['author']
        name = request.data['name']
        date = request.data['date']
        description = request.data['description']
        city = request.data['city']
        data = Activity(
            author=author,
            name=name,
            date=date,
            description=description,
            city=city
        )
        data.save()
        return HttpResponse("New activity created!")
    
    def update (self, request, *args, **kwargs):
        return HttpResponse("Activity updated!")
    
    def delete (self, request, *args, **kwargs):
        author = request.data['author']
        name = request.data['name']
        data = Activity.objects.get(author=author, name=name)
        data.delete()
        return HttpResponse("Activity deleted!")