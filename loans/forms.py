from django import forms
from django.db import models
from django.db.models import fields
from .models import City, HomeLoan, CarLoan, Car_Models
from details.models import Verification

class HomeLoanForm(forms.ModelForm):
    class Meta:
        model = HomeLoan
        fields = ['state','city','purchase_price','down_payment','desired_loan']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['city'].queryset = City.objects.none()

class CarLoanForm(forms.ModelForm):
    class Meta:
        model = CarLoan
        fields = ['car_brands','car_models','purchase_price','down_payment','desired_loan']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['car_models'].queryset = Car_Models.objects.none()


class CreditScoreForm(forms.Form):
    age = forms.IntegerField()
    annual_income = forms.IntegerField()


class Verification(forms.ModelForm):
    class Meta:
        model = Verification
        fields = ['aadhar_number','pan_number']