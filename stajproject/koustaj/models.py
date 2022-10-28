from django.db import models

# Create your models here.
class Firma(models.Model):
    firma_adi = models.CharField("Firma Adı",max_length=200)
    faaliyet_alani = models.CharField("Faaliyet Alanı",max_length=50)
    il =  models.CharField("İl",max_length=50)
    ilçe = models.CharField("İlçe",max_length=50)
    posta_kodu =  models.IntegerField("Posta Kodu",blank=True, null=True)
    telefon = models.IntegerField("Telefon",blank=True, null=True)
    #tel = models.models.PhoneNumberField(_(""))
    fax = models.IntegerField("Fax",blank=True, null=True)
    eposta = models.EmailField()
    unvan = models.CharField("Ünvan",max_length=50)
    devlet_katkisi= models.BooleanField("Devlet Katkısı",default=False)
    yetkil_ad = models.CharField("Yetkili Ad",max_length=50)
    yetkili_soyad = models.CharField("Yetkili Soyad",max_length=50)

    def __str__(self):
       return self.firma_adi 

    class Meta:
        verbose_name = "Firma"
        verbose_name_plural = "Firmalar"

class Degerlendirme(models.Model):
    degerlendirme = models.BooleanField("Değerlendirme",default=False)
    staj_basvuru = models.BooleanField("Staj Başvuru Formu",default=False)
    staj_rapor = models.BooleanField("Staj Raporu",default=False)
    staj_degerlendirme = models.BooleanField("Staj Değerlendirme Formu",default=False)

    class Meta:
        verbose_name = "Değerlendirme"
        verbose_name_plural = "Değerlendirmeler"

class OgrenciBilgi(models.Model):
    ogrenci_no =  models.IntegerField("Öğrenci No",blank=True, null=True)
    ogrenci_ad = models.CharField("Ad",max_length=50)
    ogrenci_soyad = models.CharField("Soyad",max_length=50)
    ogrenci_eposta = models.EmailField("e-mail",)
    ogrenci_telefon =  models.IntegerField("Telefon",blank=True, null=True)
    #ogrenci_sifre = ağlamak
    ogrenci_fakülte = models.CharField("Fakülte",max_length=50)
    ogrenci_bölüm = models.CharField("Bölüm",max_length=50)
    ogrenci_sinif =  models.IntegerField("Sınıf",blank=True, null=True)
    ogrenci_dönem =  models.IntegerField("Dönem",blank=True, null=True)
    ogrenci_adres = models.CharField("Adres",max_length=200)
    ogrenci_dogum_tarihi = models.DateField("Doğum Tarihi",)
    ogrenci_dogum_yeri = models.CharField("Doğum Yeri",max_length=50)
    ogrenci_kayıt_tarihi = models.DateField("Öğren Kayıt Tarihi", )
    ogrenci_tcno =  models.IntegerField("TC",blank=True, null=True)

    def __str__(self):
        return f"{self.ogrenci_ad} {self.ogrenci_soyad}"

    class Meta:
        verbose_name = "Öğrenci Bilgi"
        verbose_name_plural = "Öğrenci Bilgileri"

class OgrenciBasvuru(models.Model):
    ogrenciB = models.ForeignKey(OgrenciBilgi, on_delete=models.CASCADE, null=True)
    sigorta = models.IntegerField("Sigorta",blank=True, null=True)
    uyruk = models.CharField("Uyruk",max_length=50)
    prim =  models.IntegerField("Prim",blank=True, null=True)
    staj_sorumlusu = models.CharField("Staj Sorumlusu",max_length=50)
    tarih = models.DateField("Tarih",)
    staj_tür = models.CharField("Staj Tür",max_length=50)
    baslama_tarih = models.DateField("Başlama Tarihi",)
    bitis_tarih = models.DateField("Bitiş Tarihi",)
    is_günü = models.IntegerField("İş Günü",blank=True, null=True)

    class Meta:
        verbose_name = "Öğrenci Başvuru"
        verbose_name_plural = "Öğrenci Başvuruları"

class Ogretmen(models.Model):
    sicil_no =  models.IntegerField("Sicil No",blank=True, null=True)
    ogretmen_ad = models.CharField("Ad",max_length=50)
    ogretmen_soyad = models.CharField("Soyad",max_length=50)
    ogretmen_bolum = models.CharField("Bölüm",max_length=50)
    ogretmen_fakulte = models.CharField("Fakülte",max_length=50)

    def __str__(self):
        return f"{self.ogretmen_ad} {self.ogretmen_soyad}"

    class Meta:
        verbose_name = "Öğretmen"
        verbose_name_plural = "Öğretmenler"

class Komisyon(models.Model):
    ogretmenk = models.ForeignKey(Ogretmen, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Komisyon"
        verbose_name_plural = "Komisyon"

