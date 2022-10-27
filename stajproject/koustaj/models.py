from django.db import models

# Create your models here.
class Firma(models.Model):
    firma_adi = models.CharField(max_length=50)
    faaliyet_alani = models.CharField(max_length=50)
    il =  models.CharField(max_length=50)
    ilçe = models.CharField(max_length=50)
    posta_kodu =  models.IntegerField(blank=True, null=True)
    telefon = models.IntegerField(blank=True, null=True)
    #tel = models.models.PhoneNumberField(_(""))
    fax = models.IntegerField(blank=True, null=True)
    eposta = models.EmailField()
    unvan = models.CharField(max_length=50)
    devlet_katkisi= models.BooleanField(default=False)
    yetkil_ad = models.CharField(max_length=50)
    yetkili_soyad = models.CharField(max_length=50)

class Degerlendirme(models.Model):
    degerlendirme = models.BooleanField(default=False)

class OgrenciBilgi(models.Model):
    ogrenci_no =  models.IntegerField(blank=True, null=True)
    ogrenci_ad = models.CharField(max_length=50)
    ogrenci_soyad = models.CharField(max_length=50)
    ogrenci_eposta = models.EmailField()
    ogrenci_telefon =  models.IntegerField(blank=True, null=True)
    #ogrenci_sifre = ağlamak
    ogrenci_fakülte = models.CharField(max_length=50)
    ogrenci_bölüm = models.CharField(max_length=50)
    ogrenci_sinif =  models.IntegerField(blank=True, null=True)
    ogrenci_dönem =  models.IntegerField(blank=True, null=True)
    ogrenci_adres = models.CharField(max_length=200)
    ogrenci_dogum_tarihi = models.DateField()
    ogrenci_dogum_yeri = models.CharField(max_length=50)
    ogrenci_kayıt_tarihi = models.DateField()
    ogrenci_tcno =  models.IntegerField(blank=True, null=True)

class OgrenciBasvuru(models.Model):
    ogrenciB = models.ForeignKey(OgrenciBilgi, on_delete=models.CASCADE, null=True)
    sigorta = models.IntegerField(blank=True, null=True)
    uyruk = models.CharField(max_length=50)
    prim =  models.IntegerField(blank=True, null=True)
    staj_sorumlusu = models.CharField(max_length=50)
    tarih = models.DateField()
    staj_tür = models.CharField(max_length=50)
    baslama_tarih = models.DateField()
    bitis_tarih = models.DateField()
    is_günü = models.IntegerField(blank=True, null=True)

class Ogretmen(models.Model):
    sicil_no =  models.IntegerField(blank=True, null=True)
    ogretmen_ad = models.CharField(max_length=50)
    ogretmen_soyad = models.CharField(max_length=50)
    ogretmen_bolum = models.CharField(max_length=50)
    ogretmen_fakulte = models.CharField(max_length=50)

class Komisyon(models.Model):
    ogretmenk = models.ForeignKey(Ogretmen, on_delete=models.CASCADE, null=True)

