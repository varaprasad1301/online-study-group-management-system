from django.db import models
from django.contrib.auth.models import User

class StudySession(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hosted_sessions")
    participants = models.ManyToManyField(User, related_name="study_sessions")
    scheduled_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
