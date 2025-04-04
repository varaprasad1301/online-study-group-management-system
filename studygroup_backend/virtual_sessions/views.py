from django.shortcuts import render

# Create your views here.

from .models import VirtualSession

def virtual_sessions(request):
    sessions = VirtualSession.objects.all()
    return render(request, 'virtual_sessions.html', {'sessions': sessions})
