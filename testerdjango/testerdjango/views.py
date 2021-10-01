from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data = {
        'count':'dsddsdsdsdsd4444',
    }
    return render(request, 'index.html', data)

def index2(request):
    return render(request, 'lol.html')

def index3(request):
    return render(request, 'inform.html')

def index4(request):
    return render(request, 'product.html')