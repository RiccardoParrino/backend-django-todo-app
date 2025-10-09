class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        print("Hi from Auth middleware")
        allow_any_path = [
            '/api/token/pair',
            '/api/token/refresh',
            '/api/auth/login',
            '/api/auth/createUser',
            '/api/auth/listAllUser',
        ]
        if (request.path in allow_any_path == False):
            print("token to be verified")
        response = self.get_response(request)
        return response