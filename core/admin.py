from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import FileEncryption


class FileEncryptionAdmin(admin.ModelAdmin):
    list_display = ("file_name", "uploaded", "download_link")

    def download_link(self, obj):
        url = reverse("download_file", args=[obj.id])
        return format_html('<a href="{}">Download</a>', url)

    download_link.short_description = "Download Link"


admin.site.register(FileEncryption, FileEncryptionAdmin)


admin.site.site_header = "File Encryption Storage"
admin.site.site_title = "File Encryption "
admin.site.index_title = "Welcome to File Encryption "