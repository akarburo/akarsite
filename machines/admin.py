from django.contrib import admin
from .models import Brand,SubModel
# Register your models here.


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    
    date_hierarchy = "created_date"
    list_display = ["name","created_date"]
    list_display_links= ["name","created_date"]
    search_fields = ["name"]
    list_filter = ["created_date"]
    class Meta:
        model = Brand

@admin.register(SubModel)
class SubModelAdmin(admin.ModelAdmin):
    list_display = ["name","brand","created_date"]
    class Meta:
        model = SubModel
