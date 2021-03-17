from django.contrib import admin
from .models import Brand,Service,Demand,Agent
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

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["name","company_name","agent","created_date"]
    list_display_links = ["company_name","name","created_date"]
    search_fields = ["company_name","name"]
    list_filter = ["created_date"]
    class Meta:
        model = Service

@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["name","company_name","agent","created_date"]
    list_display_links = ["company_name","name","created_date"]
    search_fields = ["company_name","name"]
    list_filter = ["created_date"]
    class Meta:
        model = Demand

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["name","last_name"]
    list_display_links = ["name","last_name"]
    class Meta:
        model = Agent