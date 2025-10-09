from django.http import HttpResponse
from token_app import service as token_service

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        allow_any_path = [
            '/api/token/pair',
            '/api/token/refresh',
            '/api/auth/login',
            '/api/auth/createUser',
            '/api/auth/listAllUser',
        ]
        if (request.path in allow_any_path == False):
            if token_service.verify(request):
                print(token_service.verify(request))
                return self.get_response(request)
            else:
                return HttpResponse("Unhautorized: Invalid token", status='401')
        return self.get_response(request)