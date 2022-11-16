from django.contrib import admin
from .models import Firma, Degerlendirme, OgrenciBilgi, OgrenciBasvuru, Ogretmen, Komisyon, Giris   


class OgrenciBilgiAdmin(admin.ModelAdmin):
    list_display = ("ogrenci_no","ogrenci_ad","ogrenci_soyad","basvurudosyasi")
    list_filter = ("ogrenci_donem","ofirma","staj_tur","ogretmen")

class OgrenciBilgiAdmin(admin.ModelAdmin):
    list_display = ("ogrenci_no","ogrenci_ad","ogrenci_soyad","basvurudosyasi")
    list_filter = ("ogrenci_donem","ofirma","staj_tur","ogretmen")

admin.site.register(Firma),
admin.site.register(Degerlendirme),
admin.site.register(OgrenciBilgi, OgrenciBilgiAdmin),
admin.site.register(OgrenciBasvuru),
admin.site.register(Ogretmen),
admin.site.register(Komisyon),
admin.site.register(Giris),



# Register your models here.
