from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Car_Models, HomeLoan, CarLoan, City, State
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import CarLoanForm, CreditScoreForm, HomeLoanForm
from rest_framework.decorators import api_view
import requests
# Create your views here.

class HomeLoanView(CreateView):
    template_name = "loans/home_loan.html"
    model = HomeLoan
    form_class = HomeLoanForm
    success_url = "/loans/credit-score"


# def load_cities(request):
#     state_id = request.GET.get('state')
#     cities = City.objects.filter(state_id=state_id).order_by('name')
#     return render(request, 'loans/city_dropdown_list_options.html', {'cities': cities})


class CarLoanView(CreateView):
    template_name = "loans/car_loan.html"
    model = CarLoan
    form_class = CarLoanForm
    success_url = "/loans/credit-score"


# def load_models(request):
#     brand_id = request.GET.get('car_brands')
#     models = Car_Models.objects.filter(brand_id=brand_id).order_by('name')
#     return render(request, 'loans/model_dropdown_list_options.html', {'models': models})


def get_credit(request):
    # if request.method == 'POST':
    #     form = CreditScoreForm(request.POST)
    #     if form.is_valid():
    #         age = form.cleaned_data['age']
    #         a_i = form.cleaned_data['annual_income']

            URL = "https://31j0q0noye.execute-api.us-east-1.amazonaws.com/hackathon/creditscore?age=22&annualIncome=948543"
            # PARMAS = { 'age':age,
            #             'annualIncome': a_i }
            response=requests.get(url = URL).json()
            eligibility_status = response['eligiblityStatus']
            if eligibility_status == 1:
                return render(request, 'loans/positive.html',{'response':response})
            return render(request, 'loans/negative.html',{'response':response})


def get_pan(request):

    URL = "https://31j0q0noye.execute-api.us-east-1.amazonaws.com/hackathon/panverify?pancard=CIHPR9246B"
    response=requests.get(url = URL).json()
    pan = response['validPan']
    if pan == 'True':
        return render(request, 'loans/verification.html',{'response':response})

class FinalView(TemplateView):
    template_name = 'loans/final.html'