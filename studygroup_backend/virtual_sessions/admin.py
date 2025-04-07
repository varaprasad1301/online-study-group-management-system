from django.contrib import admin

# Register your models here.

from .models import VirtualSession

@admin.register(VirtualSession)
class VirtualSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'scheduled_time')
    search_fields = ('title',)

 