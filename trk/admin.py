from django.contrib import admin
from .models import UserProfile, Feedback


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display  = ['user', 'display_name', 'unit_distance', 'unit_volume', 'theme_preference', 'updated_at']
    search_fields = ['user__username', 'display_name']
    list_filter   = ['unit_distance', 'unit_volume', 'theme_preference']
    readonly_fields = ['updated_at']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display  = ['user', 'category', 'submitted_at', 'message_preview']
    list_filter   = ['category', 'submitted_at']
    search_fields = ['user__username', 'message']
    readonly_fields = ['user', 'category', 'message', 'submitted_at', 'user_agent']

    def message_preview(self, obj):
        return obj.message[:80] + ('…' if len(obj.message) > 80 else '')
    message_preview.short_description = 'Message'
