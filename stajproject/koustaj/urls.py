from django.urls import path
from .  import views

urlpatterns = [
    path('', views.index),
    path("index.html", views.index), 
    path("anasayfa.html", views.anasayfa ),
    path("basvuru.html", views.basvuru ),
    path("belge.html", views.belge ),
    path("nott.html", views.nott),
    path("ogrenci.html", views.ogrenci ),
    path("login.html", views.login),
    path("anasayfaOgretmen.html", views.anasayfaOgretmen ),
    path("basvurularOgretmen.html", views.basvurularOgretmen ),
    path("kbasvurular.html", views.kbasvurular),
    path("kbasvurulistele.html", views.kbasvurulistele),
    path("kullanıcı.html", views.kullanıcı ),
    path("sifre.html", views.sifre),
    
]
