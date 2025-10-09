from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core.serializers import serialize

from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    return HttpResponse("login response")

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):

    new_user = User.objects.create_user(
        username=request.data['username'],
        email=request.data['email'],
        password=request.data['password']
    )

    return HttpResponse("create_user response")

@api_view(['GET'])
@permission_classes([AllowAny])
def list_all_users(request):
    users = User.objects.all()
    users_json = serialize('json', users)
    return HttpResponse(users_json, content_type='application/json')