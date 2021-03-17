from django.contrib import admin
from .models import Offer

# Register your models here.

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["company_name","customer","created_date"]
    list_display_links = ["company_name","customer","created_date"]
    search_fields = ["company_name","customer"]
    list_filter = ["created_date"]
    class Meta:
        model = Offer