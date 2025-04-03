from django.contrib import admin

# Register your models here.

# from django.contrib import admin
from .models import StudySession



from django.contrib import admin
from .models import StudyGroup,StudyMaterial, Notes

@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'uploaded_at')
    search_fields = ('title',)

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'created_by', 'created_at')
    search_fields = ('title', 'created_by__username')


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'host', 'scheduled_time')  # Ensure these fields exist in StudySession model
    list_filter = ('scheduled_time',)

