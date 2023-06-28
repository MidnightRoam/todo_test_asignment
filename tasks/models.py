from django.db import models


class Task(models.Model):
    """
    Model representing a task.

    Attributes:
        title (CharField): The title of the task.
        status (BooleanField): The status of the task.

    Methods:
        None

    """
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
