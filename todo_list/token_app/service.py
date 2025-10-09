import datetime

from authentication.models import User

from django.http import HttpResponse, JsonResponse

import jwt

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
        return [token, refresh_token]
    else:
        return False

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

        return token
    except:
        return False
    
def verify(request):
    token = request.headers['Authorization'].split()[1]
    try:
        decoded = jwt.decode(token, key='mySecretKey', algorithms='HS256')
        return True
    except:
        return False