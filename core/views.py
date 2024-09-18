from django.shortcuts import render, redirect
from .forms import FileUpload
from .models import FileEncryption
from cryptography.fernet import Fernet
from django.conf import settings
from django.http import HttpResponse

def upload_file(request):
    success_message = None
    uploaded_files = FileEncryption.objects.all()  # Get the list of all uploaded files

    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['uploade_file']  

            file_data = uploaded_file.read()

            # Encrypt the file content
            encrypted_data = settings.CIPHER.encrypt(file_data)

            # Save the encrypted file in the database
            encrypted_file = FileEncryption(
                file_name=uploaded_file.name,
                encrypted_file=encrypted_data  # Save encrypted data
            )
            encrypted_file.save()

            success_message = "File uploaded and encrypted successfully!"
            uploaded_files = FileEncryption.objects.all()  # Update list after saving new file

    else:
        form = FileUpload()
    
    return render(request, 'core/upload.html', {'form': form, 'success_message': success_message, 'uploaded_files': uploaded_files})

def download_file(request, file_id):
    try:
        encrypted_file = FileEncryption.objects.get(id=file_id)

        # Decrypt the file content
        decrypted_data = settings.CIPHER.decrypt(encrypted_file.encrypted_file)

        # Send the file as an HTTP response
        response = HttpResponse(decrypted_data, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{encrypted_file.file_name}"'

        return response
    except FileEncryption.DoesNotExist:
        return HttpResponse('File not found', status=404)

def list_uploaded_files(request):
    uploaded_files = FileEncryption.objects.all()
    return render(request, 'core/file_list.html', {'uploaded_files': uploaded_files})
