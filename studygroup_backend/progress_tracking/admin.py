from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import StudyProgress, Badge, Achievement_Badge

@admin.register(StudyProgress)
class StudyProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'study_time', 'last_study_date')
    search_fields = ('user__username',)



@admin.register(Achievement_Badge)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'badge', 'earned_at')
    search_fields = ('user', 'badge')
