from django.shortcuts import render
from PIL import Image
from .forms import UploadFileForm


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            with open('name.png', 'wb+') as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)

            print(request.POST['HEX'])

            need_r = int(request.POST['HEX'][0:2], 16)
            need_b = int(request.POST['HEX'][2:4], 16)
            need_g = int(request.POST['HEX'][4:6], 16)

            img = Image.open('name.png')
            pixels = img.load()
            width, height = img.size
            pix_w = 0
            pix_b = 0
            hex = 0

            for y in range(height):
                for x in range(width):
                    r, g, b = pixels[x, y]
                    if r == 255 and g == 255 and b == 255:
                        pix_w += 1
                    if r == 0 and g == 0 and b == 0:
                        pix_b += 1

                    if r == need_r and g == need_g and b == need_b:
                        hex += 1

            print(pix_b, pix_w)
            print(hex)

            if pix_b > pix_w:
                text = "Черных пикселей больше"
            elif pix_w == pix_b:
                text = "Черных и белых одинаковое количество"
            else:
                text = "Белых пикселей больше"
            if len(request.POST['HEX']) == 6:
                text += ' пикселей выбранного вами цвета: ' + str(hex)
            return render(request, 'my_task/index.html', {'foo': text})
        else:
            print(form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'my_task/index.html', {'foo': 'baz'})
