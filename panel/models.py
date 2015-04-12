from django.db import models

# Create your models here.
class Alici(models.Model):
    kullanici_id = models.CharField(max_length=50)
    kullanici_adi = models.CharField(max_length=50)
    email = models.EmailField(blank=False)
    ad_soyad = models.CharField(max_length=100)
    sifre = models.CharField(max_length=150)
    web_site = models.CharField(max_length=80)
    token_key = models.CharField(max_length=255)
    son_giris = models.DateTimeField()
    ip_adres = models.IPAddressField()
    kayit_tarih = models.DateTimeField()

    def __unicode__(self):
        return self.ad_soyad

class Satici(models.Model):
    kullanici_id = models.CharField(max_length=50)
    kullanici_adi = models.CharField(max_length=50)
    magaza_adi = models.CharField(max_length=50)
    aciklama = models.CharField(max_length=255)
    email = models.EmailField(blank=False)
    ad_soyad = models.CharField(max_length=100)
    sifre = models.CharField(max_length=150)
    web_site = models.CharField(max_length=80)
    token_key = models.CharField(max_length=255)
    son_giris = models.DateTimeField()
    ip_adres = models.IPAddressField()
    kayit_tarih = models.DateTimeField()

    def __unicode__(self):
        return self.ad_soyad