from django.db import models
from django.utils.timezone import now


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        """A string representation of the model."""
        return self.title
