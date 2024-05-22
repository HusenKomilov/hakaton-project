from django.contrib import admin
from hospital import models


class HospitalGallery(admin.TabularInline):
    pk = "hospital"
    model = models.HospitalGallery
    extra = 1


@admin.register(models.Hospital)
class HosptialAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [HospitalGallery]


admin.site.register(models.Doctor)
admin.site.register(models.Specialty)
