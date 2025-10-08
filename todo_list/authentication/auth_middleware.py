class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        print("Hi from Auth middleware")
        response = self.get_response(request)
        return response