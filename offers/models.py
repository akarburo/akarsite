from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Offer(models.Model):
    customer = models.CharField(max_length=50,verbose_name="İsim Soyisim")
    company_name = models.CharField(max_length=100,verbose_name="Firma")
    phone = PhoneNumberField(verbose_name="Telefon Numaranız")
    mail = models.EmailField(verbose_name="E-Mail Adresiniz")
    content = models.TextField(max_length=1000,verbose_name="Açıklama")
    created_date = models.DateTimeField(auto_now_add= True,verbose_name="Oluşturma Tarihi")
    def __str__(self):
        return self.company_name

