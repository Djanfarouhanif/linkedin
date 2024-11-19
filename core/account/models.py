from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class custumeUser(AbstractUser):
    # Ajout des champs spécifiques si nécessaire
    custom_field = models.CharField(max_length=100, blank=True, null=True)

    # Résolution des conflits
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Nouveau related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Nouveau related_name
        blank=True,
    )
