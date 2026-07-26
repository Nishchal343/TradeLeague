from django.utils.cache import add_never_cache_headers


class AuthenticatedNoCacheMiddleware:
    """Ensure protected pages are revalidated after logout instead of restored from cache."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if getattr(request, "user", None) and request.user.is_authenticated:
            add_never_cache_headers(response)
        return response
