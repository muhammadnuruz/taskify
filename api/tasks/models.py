from django.db import models
from django.conf import settings
from api.teams.models import Team

class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'low', 'Past'
        MEDIUM = 'medium', 'O\'rta'
        HIGH = 'high', 'Yuqori'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='assigned_tasks'
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='tasks'
    )
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title