from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render #this line is to render HTML
from django.views.decorators.clickjacking import xframe_options_exempt
from django.urls import reverse
from . models import Document
from . forms import DocumentForm
from .services import send_to_server

maximum = 5

#list.html, called at root url:
@xframe_options_exempt
def list_view(request):
    print("貴方は Python 3.6+ を使用しています。ここで失敗した場合は、正しいバージョンを使用してください。")
    #message = 'どんな数でのファイルをアップロードして下さい！'
    message = f'ファイルを {maximum} つまで選択してください'
    message_start = 'ファイルを'
    message_end = 'つまで選択してください'
    # Handle file upload
    if Document.objects: documents_count = Document.objects.count()
    if documents_count < maximum:
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                files = request.FILES.getlist('docfile')
                if documents_count + len(files) <= maximum:
                    for f in files:
                        if request.method == 'POST' and f:
                            newdoc = Document(docfile=f)
                            newdoc.save()

                # Redirect to the document list after POST
                return redirect('list-view')
            else:
                message = 'フォームが無効でございます。このエラーを修正して下さい：'
    
    form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message, 'maximum': maximum, 'documents_count': documents_count, 'message_start': message_start, 'message_end': message_end}
    return render(request, 'list.html', context)

def send_all(request):
    # Load documents for the list page
    documents = Document.objects.all()

    #send_to_server("D:/Docs/Website/sea/upload_form/media/home/ec2-user/test/pdf/*")
    if documents:
        for document in documents: #document is a model (reference) in the database
            if document.docfile: #docfile is the actual file on disk. Here I check if the file is not deleted manually from tosend folder
                send_to_server(document.docfile.url)
                document.docfile.delete()
            if document: document.delete() #remove the file reference from the database
    else:
        text = 'no documents selected'

    return HttpResponseRedirect(reverse('list-view'))

def cancel_all(request):
    # Remove database references and the files themselves
    #docfile is the actual file on disk. Here I check if the file is not deleted manually from tosend folder
    documents = Document.objects.all()

    if documents:
        for document in documents: 
            if document.docfile: document.docfile.delete() #docfile is the actual file on disk
            if document: document.delete() #document is a model (reference) in the database
    else:
        text = 'no documents selected'

    return HttpResponseRedirect(reverse('list-view'))

def delete(request, id):
    document = Document.objects.get(id=id)
    if document.docfile: document.docfile.delete() #docfile is the actual file on disk
    if document: document.delete() #document is a model (reference) in the database
    return HttpResponseRedirect(reverse('list-view'))


