from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('SUPERADMIN', 'Super Administrador'),
        ('PADRON', 'Administrador del Padrón'),
        ('ELECCION', 'Administrador Electoral'),
        ('JURADO', 'Jurado Electoral'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='Los grupos a los que pertenece este usuario.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
