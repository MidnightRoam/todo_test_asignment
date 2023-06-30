from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView

from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm


class IndexTemplateView(TemplateView):
    """
    Class-based view for displaying the index page.

    Attributes:
        template_name (str): The name of the template to render.

    Methods:
        get_context_data(**kwargs): Adds additional context data to the view's context dictionary.

    """
    template_name = 'tasks/index.html'

    def get_context_data(self, **kwargs):
        """Add additional context data to the view's context dictionary.

        This method is called to retrieve the context data that will be used to render the template.
        It adds the 'title' variable to the context dictionary, which will be accessible in the template.

        Returns:
            dict: A dictionary containing the context data for the view.
        """
        context = super().get_context_data()
        context.update({
            'title': 'Task.IO'
        })
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
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

    form_class = TaskCreateForm
    template_name = 'tasks/task_list.html'
    model = Task
    paginate_by = 5
    success_url = reverse_lazy('tasks')
    login_url = reverse_lazy('login')

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
            'title': 'Tasks'
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


class TaskUpdateView(UpdateView):
    """A class-based view for updating a Task object.

    This view allows users to update an existing Task object using a form. It extends Django's UpdateView,
    which provides built-in functionalities for handling form processing and database updates.

    Attributes:
        template_name (str): The name of the template used to render the update task page.
        model (class): The model class associated with this view, which is Task in this case. It defines
                       the database model that this view will interact with.
        form_class (class): The form class used for updating the task. It is set to TaskUpdateForm,
                            which contains the necessary fields for updating the task instance.
        success_url (str): The URL to redirect the user to after successfully updating the task. It is set
                           to 'tasks', which is the URL name for the tasks list page.

    Methods:
        get_context_data(**kwargs):
            Returns a dictionary containing the updated context data to be used in the template rendering.
    """
    template_name = 'tasks/update_task.html'
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        """Add additional context data to be passed to the template during rendering.

        This method overrides the get_context_data() method of the parent class to add additional context data
        to be passed to the template during rendering.

        Parameters:
            **kwargs (dict): Variable keyword arguments for additional context data.

        Returns:
            dict: A dictionary containing the updated context data to be used in the template rendering.
                  The dictionary includes an entry with the key 'title', which holds the string 'Update task'.

        """
        context = super().get_context_data()
        context.update({
            'title': 'Update task'
        })
        return context
