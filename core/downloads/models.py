from django.db import models
from carousel.models import Carousel



#Gère la génération de fichiers téléchargeables (PDF, images).


"""
Relations :
Un téléchargement est associé à un seul carrousel."""

class Download(models.Model):
    carousel = models.OneToOneField(Carousel, on_delete=models.CASCADE, related_name="download")
    file = models.FileField(upload_to="downloads/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Download for Carousel: {self.carousel.title}"
