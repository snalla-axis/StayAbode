from django.db import models

# Create your models here.
from django.urls import reverse

STATUS_CHOICE = [
    ('progress', 'progress'),
    ('completed', 'completed'),
    ('pending', 'pending'),
]


class Todos(models.Model):
    title = models.CharField(max_length=256, null=False)
    description = models.TextField(max_length=256)
    todo_date_time = models.DateTimeField()
    status = models.TextField(max_length=20, choices=STATUS_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todo_list:details", kwargs={'pk': self.pk})

    def get_undeleted_tasks(self):
        return Todos.objects.filter(is_deleted=False)

    def get_task(self, pk):
        return Todos.objects.first(pk=pk)
