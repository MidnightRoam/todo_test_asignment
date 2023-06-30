from django.forms import ModelForm, CheckboxInput

from .models import Task


class TaskCreateForm(ModelForm):
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
        super().__init__(*args, **kwargs)
        self.fields['title'].label = ''
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input__default'


class TaskUpdateForm(ModelForm):
    """
    Form for updating Task objects.

    This form is used to update Task model instances. It specifies the fields to be displayed
    and allows customization of certain field attributes like labels and widget styles.

    Attributes:
        model: The Task model associated with the form.
        fields (tuple): A tuple containing the names of fields to be included in the form.

    Methods:
        __init__(*args, **kwargs): Initialize the form and customize field attributes.

    """
    class Meta:
        model = Task
        fields = ('title', 'status')

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and customize field attributes.

        This method overrides the __init__() method of the parent class and customizes the 'title'
        field label and widget attributes. It also applies specific styles to the 'title' field
        and changes the class attribute of the checkbox widget if applicable.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        super().__init__(*args, **kwargs)
        self.fields['title'].label = ''
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input__default'
            if isinstance(visible.field.widget, CheckboxInput):
                visible.field.widget.attrs['class'] = 'form-check-input'
