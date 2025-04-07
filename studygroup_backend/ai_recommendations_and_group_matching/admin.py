from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Courses



from django.contrib import admin
from .models import Courses, Quiz

@admin.register(Courses)
class TechnicalConstraintAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('technical_constraint', 'question', 'correct_answer')
    search_fields = ('technical_constraint__title', 'question')

############################################


# from django.contrib import admin
# from django.http import HttpResponseRedirect
# from django.urls import path
# from django.utils.html import format_html
# from .models import ChatbotLink, Courses, Quizzes

# @admin.register(ChatbotLink)
# class ChatbotAdmin(admin.ModelAdmin):
#     change_list_template = "admin/chatbot_entry.html"
    
#     def has_add_permission(self, request):
#         return False

#     def has_change_permission(self, request, obj=None):
#         return False

#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path('chat/', self.admin_site.admin_view(self.redirect_to_chatbot))
#         ]
#         return custom_urls + urls

#     def redirect_to_chatbot(self, request):
#         return HttpResponseRedirect("https://chatbot-8z7v.onrender.com")


# from django.contrib import admin
# from django.urls import path
# from django.http import HttpResponseRedirect
# from .models import ChatbotLink, Courses

# @admin.register(ChatbotLink)
# class ChatbotAdmin(admin.ModelAdmin):
#     change_list_template = "admin/chatbot_entry.html"

#     def changelist_view(self, request, extra_context=None):
#         # Don't touch DB at all
#         return HttpResponseRedirect("https://chatbot-8z7v.onrender.com")

#     def has_add_permission(self, request):
#         return False
#     def has_change_permission(self, request, obj=None):
#         return False


from django.contrib import admin
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import ChatbotLink

@admin.register(ChatbotLink)
class ChatbotAdmin(admin.ModelAdmin):
    change_list_template = "admin/chatbot_iframe.html"

    def changelist_view(self, request, extra_context=None):
        context = dict(
            self.admin_site.each_context(request),
            title="AI Chatbot Assistant 🤖",
        )
        return TemplateResponse(request, "admin/chatbot_iframe.html", context)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
