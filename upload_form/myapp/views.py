from django.shortcuts import redirect, render #this line is to render HTML
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import Document
from .forms import DocumentForm

'''
list.html, called at root url
'''
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
    test = render(request, 'list.html', context)
    test ['Content-Security-Policy'] = "frame-ancestors 'self' 3.115.9.253/"
    return test

from django import template
register = template.Library()

@register.simple_tag
def go_to_url(url):
    return "window.location='" + url +"'; return false;"