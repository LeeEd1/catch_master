from django.db import models
from django.contrib.auth.models import User

class CatchEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False, default="")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(blank=False, null=False, default="")
    description = models.TextField(blank=False, null=False, default="")

    def __str__(self):
        return self.name