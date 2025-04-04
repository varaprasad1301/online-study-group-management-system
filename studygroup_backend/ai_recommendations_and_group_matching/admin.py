from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Courses

# @admin.register(Courses)
# class TechnicalConstraintAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#     search_fields = ('title',)

from django.contrib import admin
from .models import Courses, Quiz

@admin.register(Courses)
class TechnicalConstraintAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('technical_constraint', 'question', 'correct_answer')
    search_fields = ('technical_constraint__title', 'question')

############################################


