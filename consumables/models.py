from django.db import models

# Create your models here.

class Toner(models.Model):
    brand = models.ForeignKey("machines.Brand", on_delete= models.CASCADE,verbose_name="Marka")
    name = models.CharField(max_length=50,verbose_name="Toner Modeli")
    info = models.TextField(default="",verbose_name="Açıklama")
    created_date = models.DateTimeField(auto_now_add= True,verbose_name="Oluşturma Tarihi")
    def __str__(self):
        return self.name

