from django.core.paginator import Paginator
from django.views.generic import ListView, TemplateView

from .models import Task


class IndexTemplateView(TemplateView):
    """
    Class-based view for displaying the index page.

    Attributes:
        template_name (str): The name of the template to render.

    Methods:
        None

    """
    template_name = 'tasks/index.html'


class TaskListView(ListView):
    """
    Class-based view for displaying a list of tasks.

    Attributes:
        model (Model): The model class to use for retrieving the data.
        template_name (str): The name of the template to render.
        paginate_by (int): The number of items to display per page.

    Methods:
        get_context_data(): Returns the context data to be used in the template.

    """
    model = Task
    template_name = 'tasks/task_list.html'
    paginate_by = 5

    def get_context_data(self):
        """
        Returns the context data to be used in the template.

        Returns:
            dict: The context data.

        """
        context = super(TaskListView, self).get_context_data()
        p = Paginator(Task.objects.all(), self.paginate_by)
        tasks = p.page(context['page_obj'].number)
        total_tasks = len(Task.objects.all())

        context.update({
            'tasks': tasks,
            'total_tasks': total_tasks
        })

        return context
