import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import jwt

from authentication.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from . import service

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def pair(request):
    return service.pair(request)

@api_view(['POST'])
@permission_classes([AllowAny])
def refresh(request):
    return service.refresh(request)

@api_view(['POST'])
@permission_classes([AllowAny])
def verify(request):
    return service.verify(request)