from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import FileEncryption, ActionLog


class FileEncryptionAdmin(admin.ModelAdmin):
    list_display = ("file_name", "uploaded", "download_link")

    def download_link(self, obj):
        url = reverse("download_file", args=[obj.id])
        return format_html('<a href="{}">Download</a>', url)

    download_link.short_description = "Download Link"


class ActionLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'file', 'timestamp', 'additional_info')
    list_filter = ('action', 'timestamp')
    search_fields = ('user__username', 'file__file_name', 'additional_info')
    readonly_fields = ('user', 'action', 'file', 'timestamp', 'additional_info')
    
    def has_add_permission(self, request):
        # Prevent manual addition of logs, only allow viewing.
        return False

class ActionLogInline(admin.TabularInline):
    model = ActionLog
    fields = ('user', 'action', 'timestamp', 'additional_info')
    readonly_fields = ('user', 'action', 'timestamp', 'additional_info')
    extra = 0
    can_delete = False
    verbose_name = "File Action Log"
    verbose_name_plural = "File Action Logs"

    def has_add_permission(self, request, obj=None):
        return False  # Disallow adding logs from inline admin

@admin.register(FileEncryption)
class FileEncryptionAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'owner', 'uploaded', 'updated')
    search_fields = ('file_name', 'owner__username')
    inlines = [ActionLogInline]

admin.site.register(ActionLog, ActionLogAdmin)

admin.site.site_header = "File Encryption Storage"
admin.site.site_title = "File Encryption "
admin.site.index_title = "Welcome to File Encryption "