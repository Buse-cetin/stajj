from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("merhaba")

def anasayfa(request):
    return render(request, 'anasayfa.html')

def basvuru(request):
    return render(request, 'basvuru.html')

def belge(request):
    return render(request, 'belge.html')

def ogrenci(request):
    return render(request, 'ogrenci.html')

def nott(request):
    return render(request, 'nott.html')