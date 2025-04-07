# # from django.shortcuts import render

# # # # Create your views here.
# # # from rest_framework import generics, permissions
# # # from rest_framework.response import Response
# # # from rest_framework.views import APIView
# # # from django.contrib.auth.models import User
# # # from .models import StudyGroup
# # # from .serializers import StudyGroupSerializer

# # # from django.urls import path

# # # # Create Study Group
# # # class CreateStudyGroupView(generics.CreateAPIView):
# # #     queryset = StudyGroup.objects.all()
# # #     serializer_class = StudyGroupSerializer
# # #     permission_classes = [permissions.IsAuthenticated]

# # #     def perform_create(self, serializer):
# # #         serializer.save(created_by=self.request.user)

# # # # Join/Leave Study Group
# # # class JoinLeaveStudyGroupView(APIView):
# # #     permission_classes = [permissions.IsAuthenticated]

# # #     def post(self, request, pk):
# # #         study_group = StudyGroup.objects.get(pk=pk)
# # #         user = request.user

# # #         if user in study_group.members.all():
# # #             study_group.members.remove(user)
# # #             return Response({"message": "Left the group"}, status=200)
# # #         else:
# # #             study_group.members.add(user)
# # #             return Response({"message": "Joined the group"}, status=200)

# # # # View Study Group Details
# # # class StudyGroupDetailView(generics.RetrieveAPIView):
# # #     queryset = StudyGroup.objects.all()
# # #     serializer_class = StudyGroupSerializer
# # #     permission_classes = [permissions.IsAuthenticated]
# # from django.shortcuts import get_object_or_404
# # from rest_framework import generics, permissions
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from django.contrib.auth.models import User
# # from .models import StudyGroup
# # from .serializers import StudyGroupSerializer

# # # Create Study Group
# # class CreateStudyGroupView(generics.CreateAPIView):
# #     queryset = StudyGroup.objects.all()
# #     serializer_class = StudyGroupSerializer
# #     permission_classes = [permissions.IsAuthenticated]

# #     def perform_create(self, serializer):
# #         serializer.save(created_by=self.request.user)

# # # Join/Leave Study Group
# # class JoinLeaveStudyGroupView(APIView):
# #     permission_classes = [permissions.IsAuthenticated]

# #     def post(self, request, pk):
# #         study_group = get_object_or_404(StudyGroup, pk=pk)
# #         user = request.user

# #         if user in study_group.members.all():
# #             study_group.members.remove(user)
# #             return Response({"message": "Left the group"}, status=200)
# #         else:
# #             study_group.members.add(user)
# #             return Response({"message": "Joined the group"}, status=200)

# # # View Study Group Details
# # class StudyGroupDetailView(APIView):
# #     permission_classes = [permissions.IsAuthenticated]

# #     def get(self, request, pk):
# #         study_group = get_object_or_404(StudyGroup, pk=pk)
# #         serializer = StudyGroupSerializer(study_group)
# #         return Response(serializer.data, status=200)

# # # material View
# # # from rest_framework.views import APIView
# # # from rest_framework.response import Response
# # # from rest_framework.parsers import MultiPartParser, FormParser
# # # from rest_framework import status
# # # from .models import StudyMaterial
# # # from .serializers import StudyMaterialSerializer

# # # class StudyMaterialUploadView(APIView):
# # #     parser_classes = (MultiPartParser, FormParser)

# # #     def post(self, request, *args, **kwargs):
# # #         file_serializer = StudyMaterialSerializer(data=request.data)
# # #         if file_serializer.is_valid():
# # #             file_serializer.save()
# # #             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
# # #         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework.parsers import MultiPartParser, FormParser
# # from rest_framework import status
# # from .models import StudyMaterial, StudyGroup
# # from .serializers import StudyMaterialSerializer, StudyGroupSerializer

# # class StudyMaterialUploadView(APIView):
# #     parser_classes = (MultiPartParser, FormParser)

# #     def post(self, request, *args, **kwargs):
# #         group_id = request.data.get("group")  # ✅ Get group ID from request
# #         try:
# #             study_group = StudyGroup.objects.get(id=group_id)
# #         except StudyGroup.DoesNotExist:
# #             return Response({"error": "Study group not found"}, status=status.HTTP_404_NOT_FOUND)

# #         request.data["group"] = study_group.id  # ✅ Assign the group ID

# #         file_serializer = StudyMaterialSerializer(data=request.data)
# #         if file_serializer.is_valid():
# #             file_serializer.save()
# #             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # class StudyMaterialListView(APIView):
# #     def get(self, request, group_id, *args, **kwargs):
# #         try:
# #             study_group = StudyGroup.objects.get(id=group_id)
# #         except StudyGroup.DoesNotExist:
# #             return Response({"error": "Study group not found"}, status=status.HTTP_404_NOT_FOUND)

# #         materials = StudyMaterial.objects.filter(group=study_group)
# #         serializer = StudyMaterialSerializer(materials, many=True)
# #         return Response(serializer.data, status=status.HTTP_200_OK)

# # class StudyGroupListView(APIView):
# #     def get(self, request, *args, **kwargs):
# #         groups = StudyGroup.objects.all()
# #         serializer = StudyGroupSerializer(groups, many=True)
# #         return Response(serializer.data, status=status.HTTP_200_OK)
# # #Study sessions
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from .models import Notes, StudyMaterial, StudyGroup, StudySession
# from .serializers import NotesSerializer, StudyMaterialSerializer, StudySessionSerializer
# from django.shortcuts import get_object_or_404

# class NotesListView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, group_id):
#         study_group = get_object_or_404(StudyGroup, id=group_id)
#         if request.user not in study_group.members.all():
#             return Response({"error": "You must join this group to view notes."}, status=status.HTTP_403_FORBIDDEN)
        
#         notes = Notes.objects.filter(group__name=study_group.name)
#         serializer = NotesSerializer(notes, many=True)
#         return Response(serializer.data)


# class StudyMaterialListView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, group_id):
#         study_group = get_object_or_404(StudyGroup, id=group_id)
#         if request.user not in study_group.members.all():
#             return Response({"error": "You must join this group to view materials."}, status=status.HTTP_403_FORBIDDEN)
        
#         materials = StudyMaterial.objects.filter(group__name=study_group.name)
#         serializer = StudyMaterialSerializer(materials, many=True)
#         return Response(serializer.data)


# class StudySessionListView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, group_id):
#         study_group = get_object_or_404(StudyGroup, id=group_id)
#         if request.user not in study_group.members.all():
#             return Response({"error": "You must join this group to view sessions."}, status=status.HTTP_403_FORBIDDEN)
        
#         sessions = StudySession.objects.filter(title__icontains=study_group.name)
#         serializer = StudySessionSerializer(sessions, many=True)
#         return Response(serializer.data)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import StudyGroup, Notes, StudyMaterial, StudySession
from .serializers import (
    StudyGroupSerializer,
    NotesSerializer,
    StudyMaterialSerializer,
    StudySessionSerializer
)
from django.shortcuts import get_object_or_404


class CreateStudyGroupView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = StudyGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JoinLeaveStudyGroupView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, group_id):
        group = get_object_or_404(StudyGroup, id=group_id)
        if request.user in group.members.all():
            group.members.remove(request.user)
            return Response({"message": "Left the group"}, status=status.HTTP_200_OK)
        else:
            group.members.add(request.user)
            return Response({"message": "Joined the group"}, status=status.HTTP_200_OK)


class StudyGroupDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, group_id):
        group = get_object_or_404(StudyGroup, id=group_id)
        serializer = StudyGroupSerializer(group)
        return Response(serializer.data)


class NotesListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, group_id):
        group = get_object_or_404(StudyGroup, id=group_id)
        if request.user not in group.members.all():
            return Response({"error": "You must join this group to view notes."}, status=status.HTTP_403_FORBIDDEN)

        notes = Notes.objects.filter(group=group)
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)


from rest_framework.parsers import MultiPartParser, FormParser

class StudyMaterialUploadView(APIView):
    permission_classes = [permissions.IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, group_id):
        group = get_object_or_404(StudyGroup, id=group_id)
        data = request.data.copy()
        data['group'] = group.id
        serializer = StudyMaterialSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StudySessionListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, group_id):
        group = get_object_or_404(StudyGroup, id=group_id)
        if request.user not in group.members.all():
            return Response({"error": "You must join this group to view sessions."}, status=status.HTTP_403_FORBIDDEN)

        sessions = StudySession.objects.filter(title__icontains=group.name)
        serializer = StudySessionSerializer(sessions, many=True)
        return Response(serializer.data)
