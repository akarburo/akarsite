from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django import forms
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50,verbose_name="Marka")
    created_date = models.DateTimeField(auto_now_add= True,verbose_name="Oluşturma Tarihi")
    def __str__(self):
        return self.name

class Demand(models.Model):
    name = models.CharField(max_length=50,verbose_name="İsim Soyisim")
    company_name = models.CharField(max_length=100,verbose_name="Firma İsmi",blank=True)
    phone = PhoneNumberField(verbose_name="Telefon Numarası")
    mail = models.EmailField(verbose_name="E-Mail")
    product = models.CharField(max_length=50,verbose_name="Teklif Almak İstediğiniz Ürün")
    quantity = models.IntegerField(verbose_name="Miktar")
    content = models.TextField(max_length=1000,verbose_name="Açıklama",blank=True)
    agent = models.ForeignKey("auth.user",on_delete=models.PROTECT,verbose_name="Temsilci",default=17)
    created_date = models.DateTimeField(auto_now_add= True,verbose_name="Oluşturma Tarihi")
    def __str__(self):
        return self.company_name

class Service(models.Model):
    name = models.CharField(max_length=50,verbose_name="İsim Soyisim",)
    company_name = models.CharField(max_length=100,verbose_name="Firma İsmi",blank=True)
    phone = PhoneNumberField(verbose_name="Telefon Numarası")
    mail = models.EmailField(verbose_name="E-Mail")
    brand = models.ForeignKey("akar.Brand", on_delete= models.PROTECT,verbose_name="Cihazınızın Markası")
    submodel = models.CharField(max_length=50,verbose_name="Cihazınızın Modeli",)
    content = models.TextField(max_length=1000,verbose_name="Açıklama")
    agent = models.ForeignKey("auth.user",on_delete=models.PROTECT,verbose_name="Temsilci",default=17)
    created_date = models.DateTimeField(auto_now_add= True,verbose_name="Oluşturma Tarihi")
    def __str__(self):
        return self.company_name

class Agent(models.Model):
    name = models.CharField(max_length=50,verbose_name="İsim")
    last_name = models.CharField(max_length=50,verbose_name="Soyisim")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
    user = models.ForeignKey("auth.user",on_delete=models.CASCADE,verbose_name="Kullanıcı Adı")
    def __str__(self):
        return self.name
    