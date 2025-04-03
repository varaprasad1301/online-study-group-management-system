from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import StudyGroup
from .serializers import StudyGroupSerializer

# Create Study Group
class CreateStudyGroupView(generics.CreateAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Join/Leave Study Group
class JoinLeaveStudyGroupView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        study_group = StudyGroup.objects.get(pk=pk)
        user = request.user

        if user in study_group.members.all():
            study_group.members.remove(user)
            return Response({"message": "Left the group"}, status=200)
        else:
            study_group.members.add(user)
            return Response({"message": "Joined the group"}, status=200)

# View Study Group Details
class StudyGroupDetailView(generics.RetrieveAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# material View
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework import status
# from .models import StudyMaterial
# from .serializers import StudyMaterialSerializer

# class StudyMaterialUploadView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request, *args, **kwargs):
#         file_serializer = StudyMaterialSerializer(data=request.data)
#         if file_serializer.is_valid():
#             file_serializer.save()
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import StudyMaterial, StudyGroup
from .serializers import StudyMaterialSerializer, StudyGroupSerializer

class StudyMaterialUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        group_id = request.data.get("group")  # ✅ Get group ID from request
        try:
            study_group = StudyGroup.objects.get(id=group_id)
        except StudyGroup.DoesNotExist:
            return Response({"error": "Study group not found"}, status=status.HTTP_404_NOT_FOUND)

        request.data["group"] = study_group.id  # ✅ Assign the group ID

        file_serializer = StudyMaterialSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudyMaterialListView(APIView):
    def get(self, request, group_id, *args, **kwargs):
        try:
            study_group = StudyGroup.objects.get(id=group_id)
        except StudyGroup.DoesNotExist:
            return Response({"error": "Study group not found"}, status=status.HTTP_404_NOT_FOUND)

        materials = StudyMaterial.objects.filter(group=study_group)
        serializer = StudyMaterialSerializer(materials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StudyGroupListView(APIView):
    def get(self, request, *args, **kwargs):
        groups = StudyGroup.objects.all()
        serializer = StudyGroupSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
