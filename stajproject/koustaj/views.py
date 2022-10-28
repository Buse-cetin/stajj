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
    ogrencis = OgrenciBasvuru.objects.all()
    return render(request, 'ogrenci.html',{'ogrencis':ogrencis} )

def login(request):
    return render(request, 'login.html')

def nott(request):
    firmas = Firma.objects.all()
    return render(request, 'nott.html',{'firmas':firmas} )

def anasayfaOgretmen(request):
    return render(request, 'anasayfaOgretmen.html')

def basvurularOgretmen(request):
    return render(request, 'basvurularOgretmen.html')

def kbasvurular(request):
    return render(request, 'kbasvurular.html')

def kbasvurulistele(request):
    return render(request, 'kbasvurulistele.html')

def kullanıcı(request):
    return render(request, 'kullanıcı.html')

def sifre(request):
    return render(request, 'sifre.html')