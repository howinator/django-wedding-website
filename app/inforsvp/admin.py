from django.contrib import admin

from .models import RSVP

# Register your models here.

@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'number_attending', 'extra_info', 'created_at')
    list_display = fields
