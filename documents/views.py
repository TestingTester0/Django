from django.shortcuts import render
from .models import Document, Test
from .forms import DocumentForm

def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', {'documents': documents})

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})

def test(request):
    questions = Test.objects.all()
    return render(request, 'test.html', {'questions': questions})