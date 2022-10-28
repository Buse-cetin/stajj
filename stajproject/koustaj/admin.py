from django.contrib import admin
from .models import Firma, Degerlendirme, OgrenciBilgi, OgrenciBasvuru, Ogretmen, Komisyon, Giris

admin.site.register(Firma),
admin.site.register(Degerlendirme),
admin.site.register(OgrenciBilgi),
admin.site.register(OgrenciBasvuru),
admin.site.register(Ogretmen),
admin.site.register(Komisyon),
admin.site.register(Giris),

# Register your models here.
