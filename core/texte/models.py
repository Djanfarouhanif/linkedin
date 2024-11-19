from django.db import models
from themes.models import Theme


#Gère la génération de contenu textuel via l'IA.

class GeneratedText(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="generated_texts")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Generated Text for Theme: {self.theme.title}"