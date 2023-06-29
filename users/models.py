# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.core.validators import MinLengthValidator, MaxLengthValidator
#
#
# class CustomUser(AbstractUser):
#     email = models.CharField(
#         validators=[
#             MinLengthValidator(6, 'Email must be at least 6 characters'),
#             MaxLengthValidator(50, 'Email should not exceed 50 characters'),
#         ]
#     )
#     password = models.CharField(
#         validators=[
#             MinLengthValidator(6, 'Password must be at least 6 characters'),
#             MaxLengthValidator(50, 'Password should not exceed 50 characters'),
#         ]
#     )
