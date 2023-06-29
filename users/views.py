from django.views.generic import TemplateView


class RegistrationTemplateView(TemplateView):
    template_name = 'users/registration.html'


class LoginTemplateView(TemplateView):
    template_name = 'users/login.html'
