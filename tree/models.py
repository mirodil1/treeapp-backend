from django.db import models
from django.conf import settings

from config.settings import env

# Create your models here.
class TimeStampModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Type(TimeStampModel):
    name = models.CharField(max_length=255, verbose_name="Turi")

    def __str__(self):
        return self.name
    

class Trees(TimeStampModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user", on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Nomi")
    image = models.ImageField(upload_to="images", default="images/tree30.11.22.11:00.jpg", blank=True)
    definition = models.TextField(blank=True, null=True, verbose_name="Ta'rif")
    latitude = models.DecimalField(max_digits=20, decimal_places=15, verbose_name="Kordinata")
    longitude = models.DecimalField(max_digits=20, decimal_places=15, verbose_name="Kordinata")
    is_verified = models.BooleanField(default=False, verbose_name="HOLATI")

    class Meta:
        verbose_name = "Daraxt"
        verbose_name_plural = "Daraxtlar"

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return env('BASE_URL') + self.image.url
        return 