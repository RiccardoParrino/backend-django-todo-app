import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import jwt

from authentication.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from . import service

# # Create your views here.
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def pair(request):
#     [access_token, refresh_token] = service.pair(request)
#     if access_token:
#         return JsonResponse({'success':'true', 'access_token':access_token, 'refresh_token':refresh_token})
#     else:
#         return JsonResponse({'success':'false', 'msg':'The credentials provided are invalid.'})

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def refresh(request):
#     token = service.refresh(request)
#     if token:
#         return JsonResponse({'success':'true', 'access_token':token})
#     else:
#         return HttpResponse("Invalid token", status='401')

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def verify(request):
#     if service.verify(request):
#         return HttpResponse("Valid token", status='200')
#     else:
#         return HttpResponse("Invalid token", status='401')
    
from rest_framework_simplejwt.views import TokenObtainPairView

from token_app.serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer