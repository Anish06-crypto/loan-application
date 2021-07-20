from details.views import BorrowerDetailView, BorrowerUpdateView, CoBorrowerView, CobUpdateView, DependantsView, GoalsView, LoanBorrowerDetailsView, LoanBorrowerMoreDetailsView
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('info/',LoanBorrowerDetailsView.as_view(),name='basic-view'),
    path('<int:pk>/info-update/',BorrowerUpdateView.as_view(),name='basic-update'),
    path('more-info/',LoanBorrowerMoreDetailsView.as_view(), name='more-view'),
    path('dependant-info/',DependantsView.as_view(), name='dep-view'),
    # path('<int:pk>/dep-update/',DepUpdateView.as_view(),name='dep-update'),
    path('coborrower-info/',CoBorrowerView.as_view(), name='cob-view'),
    path('<int:pk>/cob-update/',CobUpdateView.as_view(),name='cob-update'),
    path('details-view/<int:pk>', BorrowerDetailView.as_view(), name='details-view'),
    path('your-goals/', GoalsView.as_view(), name='goals')
    ]