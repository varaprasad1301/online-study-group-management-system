# from django.shortcuts import render

# # Create your views here.

# from .models import VirtualSession

# def virtual_sessions(request):
#     sessions = VirtualSession.objects.all()
#     return render(request, 'virtual_sessions.html', {'sessions': sessions})
 
from django.shortcuts import render, get_object_or_404
from .models import VirtualSession

def virtual_sessions(request):
    sessions = VirtualSession.objects.all()
    selected_session = None
    session_id = request.GET.get('session_id')
    if session_id:
        selected_session = get_object_or_404(VirtualSession, id=session_id)
    return render(request, 'virtual_sessions.html', {
        'sessions': sessions,
        'selected_session': selected_session
    })
