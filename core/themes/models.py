from django.db import models
from account.models import custumeUser

#Gère les thèmes soumis par les utilisateurs.

class Theme(models.Model):
    user = models.ForeignKey(custumeUser, on_delete=models.CASCADE, related_name="themes")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title