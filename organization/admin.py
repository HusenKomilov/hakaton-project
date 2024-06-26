from django.contrib import admin
from .models import Organization
# Register your models here.


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['organization_name']
    search_fields = ['organization_name', "total_money"]
