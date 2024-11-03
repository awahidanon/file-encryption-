from django.db import models
from django.contrib.auth.models import User
import uuid


class FileEncryption(models.Model):
    file_name = models.CharField(max_length=200, null=True, blank=True)
    uploade_file = models.FileField(upload_to="images/")
    encrypted_file = models.BinaryField()
    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_files', blank=True)
    share_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    


    def __str__(self):
        return self.file_name
    
    def __str__(self):
        return self.file_name

    def get_absolute_url(self):
        return reverse("download_file", args=[self.id])



class ActionLog(models.Model):
    ACTION_CHOICES = [
        ('upload', 'Upload'),
        ('share', 'Share'),
        ('download', 'Download'),
        ('view', 'View'),
    ]

    file = models.ForeignKey(FileEncryption, on_delete=models.CASCADE, related_name="action_logs")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} {self.action} {self.file.file_name} on {self.timestamp}"