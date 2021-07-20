from django.db import models
from django.core.validators import RegexValidator
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


# Create your models here.

DIFF_CHOICES = (
    ('M','male'),
    ('F', 'female'),
)

MARITAL_CHOICES = (
    ('Married','married'),
    ('Unmarried', 'unmarried'),
    ('Separated','separated'),
)

STATE_CHOICES = (
    ('Karnataka','karnataka'),
    ('Maharashtra','maharashtra'),
    ('New York','new york'),
    ('Texas','texas'),
    ('Melbourne','melbourne'),
)

COUNTRY_CHOICES = (
    ('India','India'),
    ('USA','USA'),
    ('Australia','Australia'),
)




class PersonalDetails(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=6, choices=DIFF_CHOICES, null=True)
    phone_regex = RegexValidator(regex=r'^\d{10,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, null=True) # validators should be a list
    email = models.EmailField(null=True)

    def __str__(self):
        return self.first_name

class DependantDetails(models.Model):
    age = models.IntegerField()
    borrower_name = ForeignKey(PersonalDetails, on_delete=CASCADE)


class CoBorrowerDetails(models.Model):
    borrower_name = ForeignKey(PersonalDetails, on_delete=CASCADE)
    co_borrower_name = models.CharField(max_length=100)
    cob_age = models.IntegerField()
    annual_income = models.IntegerField()

class Verification(models.Model):
    aadhar_regex = RegexValidator(regex=r'^\d{12,12}$', message="Aadhar number must be entered in the format: '1111 1111 1111 1111'. Up to 12 digits allowed.")
    aadhar_number = models.CharField(validators=[aadhar_regex],null=True, max_length=12, blank=True) # validators should be a list
    pan_regex = RegexValidator(regex=r'^[A-Za-z]{5}\d{4}[A-Za-z]{1}$', message="Pan number must be entered in the format: 'AhsGr2783d'. Up to 10 digits allowed.")
    pan_number = models.CharField(validators=[pan_regex],null=True, max_length=10, blank=True) # validators should be a list
    name = ForeignKey(PersonalDetails, on_delete=CASCADE, null=True)

class MoreDetails(models.Model):
    name = models.ForeignKey(PersonalDetails, on_delete=CASCADE)
    marital_status = models.CharField(max_length=10,null=True, choices=MARITAL_CHOICES)
    address = models.CharField(max_length=150,null=True)
    state = models.CharField(max_length=30,null=True, choices=STATE_CHOICES)
    pincode_regex = RegexValidator(regex=r'^\d{6,6}$', message="Pin number must be entered in the format: '99999'. Up to 6 digits allowed.")
    pin_code = models.CharField(validators=[pincode_regex],null=True, max_length=6, blank=True) # validators should be a list
    country = models.CharField(max_length=30,null=True, choices=COUNTRY_CHOICES)
    mailing_address = models.BooleanField(null=True)
    b_name = models.ForeignKey(DependantDetails, on_delete=CASCADE, null=True)
    cb_name = models.ForeignKey(CoBorrowerDetails, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.name.first_name



    


