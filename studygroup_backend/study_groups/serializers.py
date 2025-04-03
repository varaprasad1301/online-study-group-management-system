from rest_framework import serializers
from .models import StudyGroup

class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = '__all__'

from rest_framework import serializers
from .models import StudyMaterial

class StudyMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = "__all__"
