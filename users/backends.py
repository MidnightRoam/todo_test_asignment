from django.contrib.auth.backends import ModelBackend
from .models import CustomUser


class CustomUserBackend(ModelBackend):
    """
    Custom User Authentication Backend

    This backend allows authentication using the email field of the CustomUser model.
    It extends the ModelBackend provided by Django and overrides the authenticate method.

    Methods:
        authenticate(request, username=None, password=None, **kwargs):
            Authenticate a user based on the provided username (email) and password.

    Example Usage:
        In settings.py, configure the AUTHENTICATION_BACKENDS to use this custom backend:
        AUTHENTICATION_BACKENDS = ['your_app.backends.CustomUserBackend',]

    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Authenticate a user based on the provided email (username) and password.

        Args:
            request (HttpRequest): The current HTTP request object.
            username (str): The email address of the user attempting to log in.
            password (str): The password provided by the user.

        Returns:
            CustomUser or None: The authenticated CustomUser object if successful,
                                None if the authentication fails.

        Raises:
            None.

        """
        try:
            user = CustomUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None
