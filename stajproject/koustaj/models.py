from django.db import models


class Degerlendirme(models.Model):
    degerlendirme = models.BooleanField("Değerlendirme",default=False,null=True)
    staj_basvuru = models.BooleanField("Staj Başvuru Formu",default=False,null=True)
    staj_rapor = models.BooleanField("Staj Raporu",default=False,null=True)
    staj_degerlendirme = models.BooleanField("Staj Değerlendirme Formu",default=False,null=True)

    class Meta:
        verbose_name = "Değerlendirme"
        verbose_name_plural = "Değerlendirmeler"



class OgrenciBilgi(models.Model):
    ogrenci_no =  models.IntegerField("Öğrenci No",blank=True, null=True)
    ogrenci_ad = models.CharField("Ad",max_length=50,null=True)
    ogrenci_soyad = models.CharField("Soyad",max_length=50,null=True)
    ogrenci_eposta = models.EmailField("e-mail",null=True)
    epostaa = models.EmailField()
    #ogrenci_sifre = ağlamak
    ogrenci_fakulte = models.CharField("Fakülte",max_length=50,null=True)
    ogrenci_bolum = models.CharField("Bölüm",max_length=50,null=True)
    ogrenci_sinif =  models.IntegerField("Sınıf",blank=True, null=True)
    ogrenci_donem =  models.IntegerField("Dönem",blank=True, null=True)
    ogrenci_adres = models.CharField("Adres",max_length=200,null=True)
    ogrenci_dogum_tarihi = models.DateField("Doğum Tarihi",null=True)
    ogrenci_dogum_yeri = models.CharField("Doğum Yeri",max_length=50,null=True)
    ogrenci_kayıt_tarihi = models.DateField("Öğren Kayıt Tarihi",null=True )
    ogrenci_tcno =  models.IntegerField("TC",blank=True, null=True)
    basvuru_dosyası = models.BooleanField("Başvuru Dosyası",default=False,null=True)
    odegerlendirme = models.ForeignKey(Degerlendirme, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.ogrenci_ad} {self.ogrenci_soyad}"

    class Meta:
        verbose_name = "Öğrenci Bilgi"
        verbose_name_plural = "Öğrenci Bilgileri"

class OgrenciBasvuru(models.Model):
    ogrenciB = models.ForeignKey(OgrenciBilgi, on_delete=models.CASCADE, null=True)
    sigorta = models.IntegerField("Sigorta",blank=True, null=True)
    uyruk = models.CharField("Uyruk",max_length=50,null=True)
    prim =  models.IntegerField("Prim",blank=True, null=True)
    staj_sorumlusu = models.CharField("Staj Sorumlusu",max_length=50,null=True)
    tarih = models.DateField("Tarih",null=True)
    staj_tur = models.CharField("Staj Tür",max_length=50,null=True)
    baslama_tarih = models.DateField("Başlama Tarihi",null=True)
    bitis_tarih = models.DateField("Bitiş Tarihi",null=True)
    is_gunu = models.IntegerField("İş Günü",blank=True, null=True)

    class Meta:
        verbose_name = "Öğrenci Başvuru"
        verbose_name_plural = "Öğrenci Başvuruları"

class Firma(models.Model):
    firma_adi = models.CharField("Firma Adı",max_length=200,null=True)
    faaliyet_alani = models.CharField("Faaliyet Alanı",max_length=50,null=True)
    il =  models.CharField("İl",max_length=50,null=True)
    ilçe = models.CharField("İlçe",max_length=50,null=True)
    posta_kodu =  models.IntegerField("Posta Kodu",blank=True, null=True)
    telefon = models.IntegerField("Telefon",blank=True, null=True)
    #tel = models.models.PhoneNumberField(_(""))
    fax = models.IntegerField("Fax",blank=True, null=True)
    eposta = models.EmailField()
    unvan = models.CharField("Ünvan",max_length=50,null=True)
    devlet_katkisi= models.BooleanField("Devlet Katkısı",default=False,null=True)
    yetkil_ad = models.CharField("Yetkili Ad",max_length=50,null=True)
    yetkili_soyad = models.CharField("Yetkili Soyad",max_length=50,null=True)
    oBasvuru = models.ForeignKey(OgrenciBasvuru, on_delete=models.CASCADE, null=True)
    adres = models.CharField("Adres",max_length=250, null=True)
    oDegerlendirme = models.ForeignKey(Degerlendirme, on_delete=models.CASCADE, null=True)
    #deneme= models.ForeignKey(auth_user, on_delete=models.CASCADE, null=True)

    def __str__(self):
       return self.firma_adi 

    class Meta:
        verbose_name = "Firma"
        verbose_name_plural = "Firmalar"


class Ogretmen(models.Model):
    sicil_no =  models.IntegerField("Sicil No",blank=True, null=True)
    ogretmen_ad = models.CharField("Ad",max_length=50,null=True)
    ogretmen_soyad = models.CharField("Soyad",max_length=50,null=True)
    ogretmen_bolum = models.CharField("Bölüm",max_length=50,null=True)
    ogretmen_fakulte = models.CharField("Fakülte",max_length=50,null=True)


    def __str__(self):
        return f"{self.ogretmen_ad} {self.ogretmen_soyad}"

    class Meta:
        verbose_name = "Öğretmen"
        verbose_name_plural = "Öğretmenler"

class Giris(models.Model):
    no =  models.IntegerField(" No",blank=True, null=True)
    ogrenci_isim = models.ForeignKey(OgrenciBilgi, on_delete=models.CASCADE, null=True)
    ogretmen_isim = models.ForeignKey(Ogretmen, on_delete=models.CASCADE, null=True)
    password = models.CharField("Şifre",max_length=50,null=True)
    epostaa = models.EmailField(null=True)

    def __str__(self):
        return f"{self.no}"

    class Meta:
        verbose_name = "Giriş Bilgileri"
        verbose_name_plural = "Giriş Bİlgileri"

class Komisyon(models.Model):
    ogretmenk = models.ForeignKey(Ogretmen, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Komisyon"
        verbose_name_plural = "Komisyon"

