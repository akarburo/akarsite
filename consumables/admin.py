from django.contrib import admin
from .models import Toner
# Register your models here.

@admin.register(Toner)
class TonerAdmin(admin.ModelAdmin):
    list_display = ["name","brand","created_date"]
    class Meta:
        model = Toner