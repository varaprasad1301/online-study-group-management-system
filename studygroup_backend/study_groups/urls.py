from django.urls import path
from .views import CreateStudyGroupView, JoinLeaveStudyGroupView, StudyGroupDetailView
from .views import StudyMaterialUploadView


urlpatterns = [
    path('create/', CreateStudyGroupView.as_view(), name='create_study_group'),
    path('<int:pk>/join_leave/', JoinLeaveStudyGroupView.as_view(), name='join_leave_study_group'),
    path('<int:pk>/', StudyGroupDetailView.as_view(), name='study_group_detail'),
   
    path("upload-material/", StudyMaterialUploadView.as_view(), name="upload-material"),
     

]

