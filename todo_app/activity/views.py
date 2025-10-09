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
        return HttpResponse("Hi from POST Activity!")
    
    def update (self, request, *args, **kwargs):
        return HttpResponse("Hi from UPDATE Activity!")
    
    def delete (self, request, *args, **kwargs):
        return HttpResponse("Hi from DELETE Activity")
