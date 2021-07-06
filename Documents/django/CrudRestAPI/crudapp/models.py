from django.db import models
from django.db.models.expressions import F

class Todo(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    completed = models.BooleanField(default=True)

    def __str__(self):
        return self.title


