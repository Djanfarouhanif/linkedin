from django.db import models
from themes.models import Theme


#Gère la génération d’images via l’IA (Stable Diffusion).

class GeneratedImage(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="generated_images")
    image = models.ImageField(upload_to="images/")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Generated Image for Theme: {self.theme.title}"