from django.forms import ModelForm

from .models import Task


class TaskForm(ModelForm):
    """Form for creating and updating a task.

    This form extends the ModelForm class and provides functionality for creating and updating
    a task. It is associated with the Task model and includes only the 'title' field.

    Attributes:
        model (class): The model class associated with the form.
        fields (list): The fields to include in the form.

    Methods:
        __init__(*args, **kwargs): Initializes the form and customizes field attributes.

    """

    class Meta:
        model = Task
        fields = ('title', )

    def __init__(self, *args, **kwargs):
        """Initialize the form and customize field attributes.

        This method overrides the __init__() method of the parent class and customizes the 'title'
        field label and widget attributes.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input__default'
