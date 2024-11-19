from django.db import models
from themes.models import Theme
from texte.models import GeneratedText
from images_generated.models import GeneratedImage

"""

Gere les carusel


Un carrousel est lié à un thème.
Chaque diapositive du carrousel peut inclure un texte et/ou une image.


"""

class Carousel(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="carousels")
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carousel for Theme: {self.theme.title}"

class CarouselSlide(models.Model):
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE, related_name="slides")
    text = models.ForeignKey(GeneratedText, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ForeignKey(GeneratedImage, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Slide {self.order} for Carousel: {self.carousel.title}"
