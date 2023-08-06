"""Auth base."""

from requests.auth import AuthBase


class ApiTokenAuth(AuthBase):
    """Class for generating API Token request headers."""

    def __init__(self, api_token):
        """Initialize the :class:`ApiTokenAuth` class."""
        self.api_token = api_token

    def __call__(self, request):
        """Generate the request headers."""
        request.headers["X-API-TOKEN"] = self.api_token
        return request
