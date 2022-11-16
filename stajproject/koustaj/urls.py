from django.urls import path
from .  import views
from xml.etree.ElementInclude import include

urlpatterns = [
    path('', views.index),
    path("index.html", views.index), 
    path("anasayfa.html", views.anasayfa ),
    path('form', views.basvuru),
    path('save', views.saveform),
    path("belge.html", views.belge ),
    path("not.html", views.nott),
    path("ogrenci.html", views.ogrenci ),
    path("anasayfaO.html", views.anasayfaO ),
    path("basvuru.html", views.bassvurular ),
    path("tümbassvurular.html", views.tümbassvurular),
    path("kullanici.html", views.kullanici ),
    path("sifre.html", views.sifre),
    path("ogrencibilgi.html", views.ogrencibilgi),
    path("staj.html", views.stajbilgilendirme),
    path("listele.html", views.listele),
    path("tümünülistele.html", views.tümünülistele),
    path("login", views.login_request, name="login"),


    
]
