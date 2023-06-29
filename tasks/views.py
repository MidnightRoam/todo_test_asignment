from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DeleteView

from .models import Task
from .forms import TaskForm


class IndexTemplateView(TemplateView):
    """
    Class-based view for displaying the index page.

    Attributes:
        template_name (str): The name of the template to render.

    Methods:
        None

    """
    template_name = 'tasks/index.html'


class TaskCreateView(CreateView, LoginRequiredMixin):
    """View for creating a new task.

    This view extends the CreateView class and provides functionality to create a new task object
    using the TaskForm. The view renders the 'tasks/task_list.html' template and handles the form
    submission to create the task. It also includes pagination for the task list.

    Attributes:
        form_class (class): The form class to use for creating the task.
        template_name (str): The name of the template to render.
        model (class): The model class to use for creating the task.
        paginate_by (int): The number of tasks to display per page.
        success_url (str): The URL to redirect to upon successful task creation.

    Methods:
        get_context_data(**kwargs): Adds additional context data to the view's context dictionary.

    """

    form_class = TaskForm
    template_name = 'tasks/task_list.html'
    model = Task
    paginate_by = 5
    success_url = reverse_lazy('tasks')
    login_url = "/"

    def get_context_data(self, **kwargs):
        """Add additional context data to the view's context dictionary.

        This method overrides the get_context_data() method of the parent class and adds
        'tasks', 'total_tasks', 'page_obj', and 'form' to the context dictionary.

        Returns:
            dict: The updated context dictionary.

        """
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        p = Paginator(Task.objects.all().order_by('-id'), self.paginate_by)
        tasks = p.page(page_obj.number)
        total_tasks = len(Task.objects.all())

        context.update({
            'tasks': tasks,
            'total_tasks': total_tasks,
            'page_obj': page_obj,
            'form': self.get_form(),
        })

        return context


class TaskDeleteView(DeleteView):
    """View for deleting a task.

    This view extends the DeleteView class and provides functionality to delete a task object.
    The view renders a confirmation page to confirm the deletion of the task. Upon confirmation,
    the task object is deleted from the database, and the user is redirected to the 'tasks' page.

    Attributes:
        model (class): The model class to use for deleting the task.
        success_url (str): The URL to redirect to upon successful task deletion.

    Methods:
        None

    """

    model = Task
    success_url = reverse_lazy('tasks')
