from django.db import models


class Dupi(models.Model):
    dupiState = models.CharField(max_length=5)
    dupiImg = models.ImageField(upload_to='dupiImages/', null=True, blank=True)

