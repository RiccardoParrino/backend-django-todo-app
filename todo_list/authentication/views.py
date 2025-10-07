from django.http import HttpResponse
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def login(request):
    return HttpResponse("login response")

@api_view(['POST'])
def create_user(request):
    return HttpResponse("create_user response")