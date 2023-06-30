from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import CustomUser


class UserLoginForm(AuthenticationForm):
    """
    A custom login form for authenticating users.

    This form inherits from Django's built-in AuthenticationForm and adds custom styling to
    the email and password fields.

    Attributes:
        email (forms.EmailField): Field for entering the user's email address.
            Widget: EmailInput with 'auth__input' CSS class.
            Label: 'Email'
            Max Length: 50

        password (forms.CharField): Field for entering the user's password.
            Widget: PasswordInput with 'auth__input' CSS class.
            Max Length: 50

    Methods:
        __init__(*args, **kwargs): Initializes the form and sets the 'auth__input' CSS class
            for all visible fields.

    """
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'auth__input',
            },
        ),
        label='Email',
        max_length=50
    ),
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'auth__input'
            }
        ),
        max_length=50
    )

    def __init__(self, *args, **kwargs):
        """
        Initializes the UserLoginForm.

        This method overrides the __init__() method of the parent class to add the 'auth__input'
        CSS class to all visible fields in the form.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'auth__input'


class UserCreateForm(UserCreationForm):
    """
    A custom user creation form based on Django's UserCreationForm.

    This form allows users to sign up with an email address, password, and repeat password.

    Attributes:
        email (forms.EmailField): Field for entering the user's email address.
            Widget: EmailInput.
            Max Length: 50

        password1 (forms.CharField): Field for entering the user's password.
            Widget: PasswordInput.
            Label: 'Password'
            Max Length: 50

        password2 (forms.CharField): Field for repeating the user's password for confirmation.
            Widget: PasswordInput.
            Label: 'Repeat password'
            Max Length: 50

    Methods:
        __init__(*args, **kwargs): Initializes the form and sets the 'auth__input' CSS class
            for all visible fields.

    """
    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput()
    )

    password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(),
        label='Password'
    )

    password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(),
        label='Repeat password'
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        """
        Initializes the UserCreateForm.

        This method overrides the __init__() method of the parent class to add the 'auth__input'
        CSS class to all visible fields in the form.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'auth__input'
