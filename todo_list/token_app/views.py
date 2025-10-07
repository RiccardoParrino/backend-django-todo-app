import datetime
import json
from django.http import JsonResponse
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
            'exp': datetime.datetime.now(),
            'token_type': 'access'
        }

        token = jwt.encode(payload=payload, key='mySecretKey')
        return JsonResponse({'success':'true', 'token':token})
    else:
        return JsonResponse({'success':'false', 'msg':'The credentials provided are invalid.'})

def refresh(request):
    return None

def verify(request):
    return None