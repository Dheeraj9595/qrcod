
# views.py

import requests
from django.shortcuts import render
from .forms import QRCodeForm
from django.shortcuts import render

# myapp/views.py


def home(request):
    return render(request, 'home.html')



def generate_qr(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            body = form.cleaned_data['body']
            size = form.cleaned_data['size']
            download = form.cleaned_data['download']
            file_type = form.cleaned_data['file']

            payload = {
                "data": data,
                "config": {
                    "body": body
                },
                "size": size,
                "download": download,
                "file": file_type
            }

            response = requests.post("https://api.qrcode-monkey.com//qr/custom", json=payload)
            qr_image_url = response.json()['imageUrl']

            return render(request, 'qr_code.html', {'qr_image_url': qr_image_url})
    else:
        form = QRCodeForm()

    return render(request, 'generate_qr.html', {'form': form})
