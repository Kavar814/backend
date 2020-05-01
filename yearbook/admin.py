from django.contrib import admin
from .models import YearbookUser, Institution, InstitutionYear, InstitutionYearProfile, Signatures 

# Register your models here.

admin.site.register(YearbookUser)
admin.site.register(Institution)
admin.site.register(InstitutionYear)
admin.site.register(InstitutionYearProfile)
admin.site.register(Signatures)
