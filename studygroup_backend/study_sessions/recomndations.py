import random
from .models import StudySession, User

def recommend_sessions(user):
    all_sessions = StudySession.objects.exclude(participants=user)
    
    if not all_sessions.exists():
        return []
    
    recommended = random.sample(list(all_sessions), min(3, len(all_sessions)))
    return recommended
