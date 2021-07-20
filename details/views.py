from django.views.generic.base import TemplateView
from details.forms import CoBorrowerForm, DependentsForm, LoanBorrowerForm, LoanBorrowerMoreForm
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView,UpdateView
from .models import CoBorrowerDetails, DependantDetails, PersonalDetails, MoreDetails

# Create your views here.

def index(request):
    return render(request,'details/index.html')

class LoanBorrowerDetailsView(CreateView):
    template_name = "details/basic_form.html"
    # @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    #def dispatch(self, *args, **kwargs):
    #    return super().dispatch(*args, **kwargs)
    model = PersonalDetails
    form_class = LoanBorrowerForm
    success_url = "/more-info"

class LoanBorrowerMoreDetailsView(CreateView):
    template_name = "details/more_details.html"
    # @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    #def dispatch(self, *args, **kwargs):
    #    return super().dispatch(*args, **kwargs)
    model = MoreDetails
    form_class = LoanBorrowerMoreForm
    success_url = "/dependant-info"

class DependantsView(CreateView):
    template_name = "details/dependents.html"
    # @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    #def dispatch(self, *args, **kwargs):
    #    return super().dispatch(*args, **kwargs)
    model = DependantDetails
    form_class = DependentsForm
    success_url = "/coborrower-info"

class CoBorrowerView(CreateView):
    template_name = "details/coborrower.html"
    # @method_decorator(decorators.allowed_users(allowed_roles=['HR','admin']))
    #def dispatch(self, *args, **kwargs):
    #    return super().dispatch(*args, **kwargs)
    model = CoBorrowerDetails
    form_class = CoBorrowerForm
    success_url = "/coborrower-info"

class BorrowerDetailView(DetailView):
    template_name = "details/display.html"
    model = MoreDetails
    context_object_name = "loanb"

class GoalsView(TemplateView):
    template_name = 'details/your_goals.html'

class LoansView(TemplateView):
    template_name = 'loans/loans.html'

class BorrowerUpdateView(UpdateView):
    template_name = 'details/basic_update.html'
    model = PersonalDetails
    fields = "__all__"
    success_url = "/coborrower-info"

# class DepUpdateView(UpdateView):
#     template_name = 'details/dep_update.html'
#     model = DependantDetails
#     fields = "__all__"
#     success_url = "/coborrower-info"

class CobUpdateView(UpdateView):
    template_name = 'details/cob_update.html'
    model = CoBorrowerDetails
    fields = "__all__"
    success_url = "/coborrower-info"


