from django.http import HttpResponse
from django.shortcuts import render
from .models import Firma, OgrenciBasvuru, Degerlendirme,OgrenciBilgi,Ogretmen

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
    return render(request, 'not.html',{'firmas':firmas} )

def anasayfaO(request):
    return render(request, 'anasayfaO.html')

def bassvurular(request):
    ogrencis = OgrenciBilgi.objects.all()
    return render(request, 'bassvurular.html',{'ogrencis':ogrencis})

def tümbassvurular(request):
    ogrenciz = OgrenciBilgi.objects.all()
    return render(request, 'tümbassvurular.html',{'ogrenciz':ogrenciz})

def kullanici(request):
    ogretmens = Ogretmen.objects.all()
    return render(request, 'kullanici.html',{'ogretmens':ogretmens})

def sifre(request):
    return render(request, 'sifre.html')

