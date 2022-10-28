from django.http import HttpResponse
from django.shortcuts import render
from .models import Firma, OgrenciBasvuru, Degerlendirme

# Create your views here.
def index(request):
    return HttpResponse("merhaba")

def anasayfa(request):
    return render(request, 'anasayfa.html')

def basvuru(request):
    return render(request, 'basvuru.html')

def belge(request):
    degerlendirmes = Degerlendirme.objects.all()
    return render(request, 'belge.html',{'degerlendirmes':degerlendirmes})

def ogrenci(request):
    return render(request, 'ogrenci.html')

def login(request):
    return render(request, 'login.html')

def nott(request):
    firmas = Firma.objects.all()
    ogrencis = OgrenciBasvuru.objects.all()
    return render(request, 'nott.html',{'firmas':firmas},{'ogrencis':ogrencis} )