from django.db import models
from django.conf import settings

class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name='Jamoa nomi')
    description = models.TextField(blank=True, null=True, verbose_name='Tavsif')
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_teams',
        verbose_name='Yaratuvchi'
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='teams',
        blank=True,
        verbose_name='A\'zolar'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name