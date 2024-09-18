from django.db import models

class FileEncryption(models.Model): 
    file_name = models.CharField(max_length=200, null=True, blank=True)
    uploade_file = models.FileField(upload_to='images/')
    encrypted_file = models.BinaryField()
    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_name
