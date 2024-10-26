import mimetypes
from docx import Document
def get_mime_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type

file_path = "/workspaces/file-encryption-/requirements.txt"
mime_type = get_mime_type(file_path)
print(f"MIME type: {mime_type}")

if mime_type and mime_type.startswith('image/'):
    #using  html5 for image and pdf
     #<img src="{{ file.url }}" alt="file description" />
    print("It is an image")
elif mime_type == 'application/pdf':
    print("It is a PDF")
    #<embed src="{{ file.url }}" width="100%" height="600px" />
elif mime_type == 'application/msword':
    print("It is a Word")
    #rendering word in html
    """
    document = Document(file.path)
    content = ""
    for para in document.paragraphs:
        content += f"<p>{para.text}</p>"
    return render(request, 'view_docx_file.html', {'content': content})
    """
elif mime_type == 'text/plain':   
    print("It is a text")
    '''file= encrypted_data
    with open(file.path, 'r') as f:
        content = f.read()
    return render(request, 'view_text_file.html', {'content': content})'''
else:
    print("Unknown file type")
    print(f"MIME type: {mime_type}")
