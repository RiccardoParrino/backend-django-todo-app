from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core.serializers import serialize

from authentication.models import User

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
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')
    surname = request.data.get('surname')
    new_user = User(
        email=email,
        password=password,
        name=name,
        surname=surname
    )
    new_user.save()
    return HttpResponse("create_user response")

@api_view(['GET'])
@permission_classes([AllowAny])
def list_all_users(request):
    users = User.objects.all()
    users_json = serialize('json', users)
    return HttpResponse(users_json, content_type='application/json')