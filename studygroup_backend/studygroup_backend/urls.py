"""
URL configuration for studygroup_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/study_groups/', include('study_groups.urls')),
# ] 

from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin  # ✅ Add this line
from django.shortcuts import render

def home_redirect(request):
    return render(request, "home.html")

urlpatterns = [
    path("",home_redirect),
    path("admin/", admin.site.urls),
    path("api/study_groups/", include("study_groups.urls")),  # Replace "your_app" with your actual app name
    path('', include('virtual_sessions.urls')),
    
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

