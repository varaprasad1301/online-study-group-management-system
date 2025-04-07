from django.shortcuts import render

# # Create your views here.

import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def chatbot_view(request):
    user = request.user
    message = request.data.get("message", "")
    
    try:
        # Forward the message to external chatbot
        response = requests.post(
            "https://chatbot-8z7v.onrender.com",
            json={"message": message, "user": user.username},
            timeout=10
        )
        if response.status_code == 200:
            return Response({"reply": response.json().get("reply", "🤖 No reply received.")})
        else:
            return Response({"reply": "❌ External chatbot error. Try again later."}, status=502)
    except Exception as e:
        return Response({"reply": f"💥 Chatbot service unavailable: {str(e)}"}, status=503)
