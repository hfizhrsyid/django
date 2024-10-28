from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cv(request):
    return render(request, 'cv.html')

def karir(request):
    return render(request, 'karir.html')

def keahlian(request):
    return render(request, 'keahlian.html')

def organisasi(request):
    return render(request, 'organisasi.html')

def pendidikan(request):
    return render(request, 'pendidikan.html')