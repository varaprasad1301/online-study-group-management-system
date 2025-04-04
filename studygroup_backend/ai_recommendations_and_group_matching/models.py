from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    # url= models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.title


class Quiz(models.Model):
    technical_constraint = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="quizzes")
    question = models.CharField(max_length=500)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)  # This will be hidden from users

    def __str__(self):
        return f"Quiz on {self.technical_constraint.title}: {self.question}"


class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=255, blank=True, null=True)
    attempted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.question}"
