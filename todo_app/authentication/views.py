from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):

    def get (self, request, *args, **kwargs):
        data = serializers.serialize("json", User.objects.all())
        return HttpResponse(data)
    
    def post(self, request, *args, **kwargs):
        user = User.objects.create_user(
            username='admin',
            email='admin',
            password='admin'
        )
        return HttpResponse('ok')