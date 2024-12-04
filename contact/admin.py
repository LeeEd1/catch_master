from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    fields = ('name', 'email', 'phone_number', 'message', 'created_at')

    list_display = ('name', 'email', 'phone_number', 'created_at')

    ordering = ('-created_at',)
