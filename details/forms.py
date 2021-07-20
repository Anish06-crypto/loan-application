from django import forms
from django.db import models
from django.db.models import fields
from .models import CoBorrowerDetails, DependantDetails, PersonalDetails,MoreDetails

class LoanBorrowerForm(forms.ModelForm):
    class Meta:
		   model = PersonalDetails
		   fields = ['first_name','last_name','birth_date','gender','phone_number','email']


class LoanBorrowerMoreForm(forms.ModelForm):
    class Meta:
		   model = MoreDetails
		   fields = ['name','marital_status','address','state','pin_code','country','mailing_address']

class DependentsForm(forms.ModelForm):
    class Meta:
            model = DependantDetails
            fields = ['borrower_name','age']

class CoBorrowerForm(forms.ModelForm):
    class Meta:
            model = CoBorrowerDetails
            fields = ['borrower_name','co_borrower_name','cob_age','annual_income']


