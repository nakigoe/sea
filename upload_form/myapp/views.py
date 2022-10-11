from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render #this line is to render HTML
from django.views.decorators.clickjacking import xframe_options_exempt
from django.urls import reverse
from . models import Document
from . forms import DocumentForm
from .services import send_to_server

'''list.html, called at root url'''
@xframe_options_exempt
def list_view(request):
    print("貴方は Python 3.6+ を使用しています。ここで失敗した場合は、正しいバージョンを使用してください。")
    message = 'どんな数でのファイルをアップロードして下さい！'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('list-view')
        else:
            message = 'フォームが無効でございます。このエラーを修正して下さい：'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)

def send_all(request):
    # Load documents for the list page
    documents = Document.objects.all()

    #send_to_server("D:/Docs/Website/sea/upload_form/media/home/ec2-user/test/pdf/*")
    if documents:
        for document in documents:
            send_to_server(document.docfile.url)
            document.delete()
    else:
        text = 'no documents selected'

    return HttpResponseRedirect(reverse('list-view'))
