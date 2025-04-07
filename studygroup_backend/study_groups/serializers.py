# from rest_framework import serializers
# from .models import StudyGroup

# class StudyGroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudyGroup
#         fields = '__all__'

# from rest_framework import serializers
# from .models import StudyMaterial

# class StudyMaterialSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudyMaterial
#         fields = "__all__"
from rest_framework import serializers
from .models import StudyGroup, StudyMaterial, Notes, StudySession
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class StudyGroupSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = StudyGroup
        fields = '__all__'

class StudyMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = '__all__'

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'

class StudySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudySession
        fields = '__all__'
