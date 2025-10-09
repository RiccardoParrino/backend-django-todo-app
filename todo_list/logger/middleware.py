from django.core.cache import cache

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        freq = cache.get(request.path)
        if freq is None:
            cache.set(request.path, 1)
        else:
            cache.set(request.path, freq+1)
        response = self.get_response(request)
        return response