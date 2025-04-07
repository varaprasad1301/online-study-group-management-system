from django.db import models

# Create your models here.
# from django.db import models
from django.contrib.auth.models import User

class StudyGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="study_groups", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

class StudySession(models.Model):
    title = models.CharField(max_length=255)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
   
    def __str__(self):
        return self.title


from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    group = models.ForeignKey('Study_Group', on_delete=models.CASCADE, related_name="notes")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
from django.db import models


class StudyMaterial(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="study_materials/")
    group = models.ForeignKey('Study_Group', on_delete=models.CASCADE, related_name="materials")  # ✅ Associate with a group
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.group.name})"

from django.contrib.auth.models import Group

class Study_Group(Group):
    class Meta:
        proxy = True  # This makes it behave like a new model without changing the database
        app_label = 'study_groups'  # Moves it under the STUDY_GROUPS section


####################################################################################

