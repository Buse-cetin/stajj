from django.urls import path
from .  import views

urlpatterns = [
    path('', views.index),
    path("index.html", views.index), 
    path("anasayfa.html", views.anasayfa ),
    path("basvuru.html", views.basvuru ),
    path("belge.html", views.belge ),
    path("not.html", views.nott),
    path("ogrenci.html", views.ogrenci ),
    path("login.html", views.login),
    path("anasayfaO.html", views.anasayfaO ),
    path("başvurular.html", views.başvurular ),
    path("tümbaşvurular.html", views.tümbaşvurular),
    path("kullanıcı.html", views.kullanıcı ),
    path("şifre.html", views.şifre),
    
]
