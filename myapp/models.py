from django.db import models


class News(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(upload_to='coffeeSort/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

# Create your models here.
