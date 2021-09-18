from django.shortcuts import render
from PIL import Image
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


            img = Image.open('name.png')
            pixels = img.load()
            width, height = img.size
            pix_w = 0
            pix_b = 0

            for y in range(height):  # this row
                for x in range(width):  # and this row was exchanged
                    r, g, b = pixels[x, y]
                    if r == 255 and g == 255 and b == 255:
                        pix_w += 1
                    if r == 0 and g == 0 and b == 0:
                        pix_b += 1
                    # in case your image has an alpha channel
                    # r, g, b, a = pixels[x, y]

            print(pix_b, pix_w)

            text = ""
            if pix_b > pix_w:
                text = "Черных пикселей больше"
            else:
                text = "Белых пикселей больше"
            return render(request, 'my_task/index.html', {'foo': text})
        else:
            print(form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'my_task/index.html', {'foo': 'baz'})
