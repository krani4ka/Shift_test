from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm


# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            with open('name.png', 'wb+') as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)
        return render(request, 'my_task/index.html', {'foo': 'bar'})
    else:
        form = UploadFileForm()
    return render(request, 'my_task/index.html', {'foo': 'baz'})
