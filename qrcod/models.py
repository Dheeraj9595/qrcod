# models.py

from django.db import models

class QRCode(models.Model):
    data = models.URLField()
    body = models.CharField(max_length=10, choices=[('square', 'Square'), ('circle', 'Circle')])
    size = models.IntegerField()
    download = models.BooleanField()
    file_type = models.CharField(max_length=10, choices=[('png', 'PNG'), ('svg', 'SVG')])
    qr_image_url = models.URLField()

    def __str__(self):
        return f"QR Code for {self.data}"

