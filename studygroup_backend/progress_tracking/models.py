from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class StudyProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study_time = models.IntegerField(help_text="Total study time in Hours")
    last_study_date = models.DateTimeField(auto_now=True)

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name  
class Achievement_Badge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.badge.name}" 