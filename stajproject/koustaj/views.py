from django.http import HttpResponse
from django.shortcuts import render
from .models import Firma, OgrenciBasvuru, Degerlendirme,OgrenciBilgi

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

def başvurular(request):
    ogrencis = OgrenciBilgi.objects.all()
    return render(request, 'başvurular.html',{'ogrencis':ogrencis})

def tümbaşvurular(request):
    ogrenciz = OgrenciBilgi.objects.all()
    return render(request, 'tümbaşvurular.html',{'ogrenciz':ogrenciz})

def kullanıcı(request):
    return render(request, 'kullanıcı.html')

def şifre(request):
    return render(request, 'şifre.html')

