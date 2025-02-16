from django.db import models

# Create your models here.
class Kyc(models.Model):
    camera_image = models.ImageField(upload_to='images/id/')
    id_image = models.ImageField(upload_to='images/camera/')