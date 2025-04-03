from celery import shared_task
from django.utils.timezone import now
from django.core.mail import send_mail
from .models import StudySession

@shared_task
def send_session_reminders():
    upcoming_sessions = StudySession.objects.filter(scheduled_time__gt=now())
    
    for session in upcoming_sessions:
        subject = f"Reminder: {session.title}"
        message = f"Your study session '{session.title}' is scheduled for {session.scheduled_time}."
        recipient_list = [user.email for user in session.participants.all()]
        # send_mail(subject, message, "99210041857@klu.ac.in", recipient_list)

        send_mail(subject, message, "admin@studygroup.com", recipient_list)
