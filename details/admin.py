from django.contrib import admin
from .models import MoreDetails, PersonalDetails,DependantDetails,CoBorrowerDetails
# Register your models here.

admin.site.register(PersonalDetails)
admin.site.register(MoreDetails)
admin.site.register(DependantDetails)
admin.site.register(CoBorrowerDetails)
