from django.db import models
import uuid

# Create your models here.

class Todo(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title