from celery import Celery

app = Celery('studygroup_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send-study-session-reminders': {
        'task': 'study_sessions.tasks.send_session_reminders',
        'schedule': 3600.0,  # Every hour
    },
}
