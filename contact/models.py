from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = "Messages"