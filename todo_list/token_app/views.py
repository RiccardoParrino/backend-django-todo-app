import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import jwt

from authentication.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def pair(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.get(email=email,password=password)

    if user is not None:
        payload = {
            'user_id': user.id,
            'username': user.email,
            'name': user.name,
            'surname': user.surname,
            'exp': datetime.datetime.now(),
            'token_type': 'access'
        }

        refresh_payload = {
            'user_id': user.id,
            'username': user.email,
            'name': user.name,
            'surname': user.surname,
            'exp': datetime.datetime.now() + datetime.timedelta(7),
            'token_type': 'access'
        }

        token = jwt.encode(payload=payload, key='mySecretKey')
        refresh_token = jwt.encode(payload=refresh_payload, key='mySecretKey')
        return JsonResponse({'success':'true', 'access_token':token, 'refresh_token':refresh_token})
    else:
        return JsonResponse({'success':'false', 'msg':'The credentials provided are invalid.'})

@api_view(['POST'])
@permission_classes([AllowAny])
def refresh(request):
    token = request.headers['Authorization'].split()[1]
    try:
        decoded = jwt.decode(token, key='mySecretKey', algorithms='HS256')

        payload = {
            'user_id': decoded['user_id'],
            'username': decoded['username'],
            'name': decoded['name'],
            'surname': decoded['surname'],
            'exp': datetime.datetime.now(),
            'token_type': 'access'
        }

        token = jwt.encode(payload=payload, key='mySecretKey')

        return JsonResponse({'success':'true', 'access_token':token})
    except:
        return HttpResponse("Invalid token", status='401')

@api_view(['POST'])
@permission_classes([AllowAny])
def verify(request):
    token = request.headers['Authorization'].split()[1]
    try:
        decoded = jwt.decode(token, key='mySecretKey', algorithms='HS256')
        return HttpResponse("Valid token", status='200')
    except:
        return HttpResponse("Invalid token", status='401')