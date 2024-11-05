from django.db import models
from django.contrib.auth.models import User

class CatchEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name