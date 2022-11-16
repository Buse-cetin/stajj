from django.http import HttpResponse
from .models import Firma, OgrenciBasvuru, Degerlendirme,OgrenciBilgi,Ogretmen,Firma, Degerlendirme
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,  login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from  koustaj.forms import basvuruForm

# Create your views here.
def index(request):
    return HttpResponse("merhaba")

def anasayfa(request):
    return render(request, 'anasayfa.html')

def basvuru(request):
    bform = basvuruForm
    return render(request, 'basvuru.html',{'bform':bform})

def saveform(request):
    bform = basvuruForm(request.POST)
    bform.save()
    return HttpResponse('başvuru eklendi')

def belge(request):
    degerlendirmes = Degerlendirme.objects.all()
    return render(request, 'belge.html',{'degerlendirmes':degerlendirmes})

def ogrenci(request):
    ogrencis = OgrenciBasvuru.objects.all()
    return render(request, 'ogrenci.html',{'ogrencis':ogrencis} )


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

def ogrencibilgi(request):
    return render(request, 'ogrencibilgi.html')



def stajbilgilendirme(request):
    return render(request, 'staj.html')
    
def listele(request):
    ogrencii = OgrenciBilgi.objects.all()
    return render(request, 'listele.html',{'ogrencii':ogrencii})

def blogs_by_category(request, slug):
    context = {
        "ogrencii": OgrenciBilgi.objects.filter(is_active=True, category__slug=slug),
        "ogrencii": OgrenciBilgi.objects.all()
    }
    return render(request, "blistele.html", context)

def tümünülistele(request):
    ogrenciy = OgrenciBilgi.objects.all()
    return render(request, 'tümünülistele.html',{'ogrenciy':ogrenciy})

def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
                    
        user = authenticate(request, username = username, password = password)
        
        if user is not None :
            login(request, user)
         
            if len(username) == 9:
                return redirect('anasayfa.html')
            elif len(username) == 4:
                return redirect('anasayfaO.html')
        else:
            return render(request,'login.html',{"error":"kullanıcı no ya da parola yanlış"})

    return render(request, 'login.html')
    

def ogrenci(request):
    current_user = request.user
    id = current_user.id
    ogrencib = OgrenciBilgi.objects.raw("SELECT * FROM koustaj_ogrencibilgi WHERE id=%s",[id])
    return render(request, 'ogrenci.html',{'data':ogrencib} )