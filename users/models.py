from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.core.validators import MinLengthValidator, MaxLengthValidator


class CustomUser(AbstractUser):
    """
    Custom user model based on Django's AbstractUser.

    This model extends the built-in user model by replacing the username field with an email field.
    The email field is unique and is used as the USERNAME_FIELD for authentication.

    Fields:
        email (models.EmailField): The email address of the user.
            Attributes:
                unique (bool): True, ensuring each email address is associated with only one user.
                validators (list): A list of MinLengthValidator and MaxLengthValidator for email length validation.
                    - MinLengthValidator: Validates that the email has at least 6 characters.
                    - MaxLengthValidator: Validates that the email does not exceed 50 characters.

    USERNAME_FIELD (str): The field used for authentication, set to 'email'.

    REQUIRED_FIELDS (list): The list of required fields for creating a superuser, set to an empty list.

    """
    email = models.EmailField(
        unique=True,
        validators=[
            MinLengthValidator(6, 'Email must be at least 6 characters'),
            MaxLengthValidator(50, 'Email should not exceed 50 characters'),
        ]
    )
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
