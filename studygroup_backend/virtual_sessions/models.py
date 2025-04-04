from django.db import models

# Create your models here.


class VirtualSession(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    scheduled_time = models.DateTimeField()
    meeting_link = models.URLField(blank=True, null=True)  # Store Google Meet/Zoom link

    def __str__(self):
        return self.title
