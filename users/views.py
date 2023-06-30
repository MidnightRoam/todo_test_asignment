from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView

from .forms import UserLoginForm, UserCreateForm


class UserLoginView(LoginView):
    """
    Class-based view for user login functionality.

    This view handles user authentication and login using Django's built-in LoginView.
    It uses a custom UserLoginForm for rendering the login form.

    Attributes:
        template_name (str): The name of the template to render for the login page.
        form_class (UserLoginForm): The form class used to render the login form.

    Methods:
        get_context_data(**kwargs): Adds additional context data to the view's context dictionary.
        get_success_url(): Returns the URL to redirect the user to upon successful login.

    """
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        """
        Returns the view's context dictionary with additional data.

        Returns:
            dict: The context dictionary with 'title' set to 'Sign In'.
        """
        context = super().get_context_data()
        context.update({
            'title': 'Sign In'
        })
        return context

    def get_success_url(self):
        """
        Returns the URL to redirect the user after successful login.

        Returns:
            str: The URL where the user will be redirected.
        """
        return reverse_lazy('tasks')


class UserCreateView(CreateView):
    """
    Class-based view for user registration (Sign Up) functionality.

    This view handles user registration and account creation using Django's built-in CreateView.
    It uses a custom UserCreateForm for rendering the registration form.

    Attributes:
        template_name (str): The name of the template to render for the registration page.
        form_class (UserCreateForm): The form class used to render the registration form.
        success_url (str): The URL to redirect the user to upon successful registration.

    Methods:
        get_context_data(**kwargs): Adds additional context data to the view's context dictionary.
        form_valid(form): Saves the form data and logs in the user upon successful registration.

    """
    template_name = 'users/registration.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        """
        Returns the view's context dictionary with additional data.

        Returns:
            dict: The context dictionary with 'title' set to 'Sign Up'.
        """
        context = super().get_context_data()
        context.update({
            'title': 'Sign Up'
        })
        return context

    def form_valid(self, form):
        """
        Saves the form data and logs in the user upon successful registration.

        Args:
            form (UserCreateForm): The valid form instance containing user registration data.

        Returns:
            HttpResponseRedirect: Redirects the user to the 'success_url'.
        """
        user = form.save()
        login(self.request, user)
        return redirect('tasks')


class UserLogout(View):
    """
    View for user logout functionality.

    This view handles user logout using Django's built-in logout() function.

    Methods:
        get(request, *args, **kwargs): Logs out the user and redirects to the 'index_page'.

    """
    def get(self, request, *args, **kwargs):
        """
        Logs out the user and redirects to the 'index_page'.

        Args:
            request (HttpRequest): The HTTP request object used to process the logout.

        Returns:
            HttpResponseRedirect: Redirects the user to the 'index_page'.
        """
        logout(request)
        return redirect('index_page')
