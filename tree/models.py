from io import BytesIO    

from django.db import models
from django.conf import settings
from django.core.files import File

from PIL import Image, ImageDraw
import qrcode

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
    image = models.ImageField(upload_to="images", default="https://cdn.pixabay.com/photo/2014/12/22/00/07/tree-576847__480.png", blank=True)
    qr_code = models.ImageField(upload_to="qr-code", default='https://cdn.pixabay.com/photo/2014/12/22/00/07/tree-576847__480.png')
    definition = models.TextField(blank=True, null=True, verbose_name="Ta'rif")
    latitude = models.DecimalField(max_digits=20, decimal_places=15, verbose_name="Kordinata")
    longitude = models.DecimalField(max_digits=20, decimal_places=15, verbose_name="Kordinata")
    is_verified = models.BooleanField(default=False, verbose_name="HOLATI")

    class Meta:
        verbose_name = "Daraxt"
        verbose_name_plural = "Daraxtlar"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.qr_code:
            qr = qrcode.QRCode(
                version=4,
                box_size=10,
                border=3
            )
            
            qr.add_data(env('BASE_CLIENT_URL')+f"/tree/{self.id}")
            qr.make()
            qrcode_img = qr.make_image(fill_color="black", back_color="white")
            canvas = Image.new('RGB', (390, 390), 'white')
            draw = ImageDraw.Draw(canvas)
            canvas.paste(qrcode_img)
            file_name = f'qr_code-{self.name}-{str(self.id)}.png'
            buffer = BytesIO()
            canvas.save(buffer, 'PNG')
            self.qr_code.save(file_name, File(buffer), save=False)
            canvas.close()
            super().save(*args, **kwargs)


    def get_image(self):
        if self.image:
            return env('BASE_URL') + self.image.url
        return 
    
    def get_qrcode(self):
        if self.qr_code:
            return env('BASE_URL') + self.qr_code.url
        return

   
