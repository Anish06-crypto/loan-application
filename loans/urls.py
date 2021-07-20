

from details.views import BorrowerDetailView, LoansView
from loans.views import FinalView, HomeLoanView, CarLoanView
from django.urls import path
from . import views

urlpatterns = [
    path('home/',HomeLoanView.as_view(),name='home-loan'),
    # path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('car/',CarLoanView.as_view(),name='car-loan'),
    # path('ajax/load-models/', views.load_models, name='ajax_load_models'),
    path('credit-score/', views.get_credit, name='credit-score'),
    path('options/', LoansView.as_view(), name='options'),
    path('verification/', views.get_pan, name='verify'),
    path('final/', FinalView.as_view(), name='final'),
    ]