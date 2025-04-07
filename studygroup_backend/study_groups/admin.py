from django.contrib import admin

# Register your models here.

# from django.contrib import admin
from .models import StudySession

admin.site.site_header = "Online Study Portal"

from django.contrib import admin
from .models import Study_Group,StudyMaterial, Notes

@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'group','uploaded_at')
    search_fields = ('title',)

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'created_by', 'created_at')
    search_fields = ('title', 'created_by__username')


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'host', 'scheduled_time')  # Ensure these fields exist in StudySession model
    list_filter = ('scheduled_time',)

from django.contrib import admin
from .models import Study_Group  # Import the proxy model

class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Unregister default Group model
from django.contrib.auth.models import Group
admin.site.unregister(Group)




from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import format_html
from django.shortcuts import redirect
from .models import Study_Group
from django.contrib.auth.models import Group

class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "join_button", "leave_button")

    def join_button(self, obj):
        url = reverse("admin:study_groups_study_group_change", args=[obj.id]) + f"?join_group={obj.id}"
        return format_html('<a class="button" onclick="return confirmJoin()" href="{}">Join</a>', url)
    
    def leave_button(self, obj):
        url = reverse("admin:study_groups_study_group_change", args=[obj.id]) + f"?leave_group={obj.id}"
        return format_html('<a class="button" style="color:red;" onclick="return confirmLeave()" href="{}">Leave</a>', url)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        # JOIN LOGIC
        if "join_group" in request.GET:
            group = Group.objects.get(id=object_id)
            request.user.groups.add(group)
            messages.success(request, f"You have joined the Group '{group.name}'.")
            return redirect(request.path)

        # LEAVE LOGIC
        if "leave_group" in request.GET:
            group = Group.objects.get(id=object_id)
            request.user.groups.remove(group)
            messages.info(request, f"You have left the study session '{group.name}'.")
            return redirect(request.path)

        return super().change_view(request, object_id, form_url, extra_context)

    class Media:
        js = ('admin/js/confirm_buttons.js',)

# Register Study_Group (proxy) with custom admin
admin.site.register(Study_Group, CustomGroupAdmin)



##app list view
