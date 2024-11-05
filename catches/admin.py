from django.contrib import admin
from .models import CatchEntry

@admin.register(CatchEntry)
class CatchEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'name')
    fields = ('user', 'name', 'image_url', 'image', 'description')

    list_display = ('name', 'user', 'description')

    ordering = ('-id',)