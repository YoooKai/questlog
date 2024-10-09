from django.db import models


# Create your models here.
class ToDoItem(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    details = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    due_date = models.DateTimeField()
    slug = models.SlugField('max_length=150', unique=True)

    def __str__(self):
        return self.task
