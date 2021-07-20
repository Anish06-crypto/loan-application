from django.contrib import admin
from .models import Car_Brands, Car_Models, City, HomeLoan, CarLoan, State
# Register your models here.

admin.site.register(State)
admin.site.register(City)
admin.site.register(Car_Brands)
admin.site.register(Car_Models)
admin.site.register(HomeLoan)
admin.site.register(CarLoan)