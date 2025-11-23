from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import LoginForm
from .models import Lead, Application, Payment, Branch
from .forms import LeadForm, ApplicationForm, PaymentForm
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .custommixins import SuperUserRequiredMixin


class LeadsListView(LoginRequiredMixin, ListView):
    model = Lead
    context_object_name = 'leads'
    ordering = '-id'
    paginate_by = 30
    template_name = 'dashboard/leads.html'
    

@login_required    
def leads_by_banch(request, pk):
    branch = get_object_or_404(Branch, id=pk)
    leads = Lead.objects.filter(branch=branch)
    page = request.GET.get('page', 1)
    paginator = Paginator(leads, 30)
    try:
        leads = paginator.page(page)
    except PageNotAnInteger:
        leads = paginator.page(1)
    except EmptyPage:
        leads = paginator.page(paginator.num_pages) 
    context = {
        'leads': leads
    }
    return render(request, 'dashboard/leads.html', context)


class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead
    template_name = 'dashboard/lead-details.html'


class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'dashboard/lead-form.html'


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = Lead
    form_class = LeadForm
    template_name = 'dashboard/lead-form.html'


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    model = Lead

    def get_success_url(self):
        return reverse('leads')


@login_required
def lead_search(request):
    query = request.GET['q']
    context = {
        'leads': Lead.objects.filter(Q(full_name__icontains=query) | Q(mobile_number__iexact=query)),
    }
    return render(request, 'dashboard/lead_search.html', context)


class ApplicationsListView(LoginRequiredMixin, ListView):
    model = Application
    context_object_name = 'applications'
    ordering = '-id'
    paginate_by = 30
    template_name = 'dashboard/applications.html'


@login_required
def applications_by_banch(request, pk):
    branch = get_object_or_404(Branch, id=pk)
    applications = Application.objects.filter(branch=branch)
    page = request.GET.get('page', 1)
    paginator = Paginator(applications, 30)
    try:
        applications = paginator.page(page)
    except PageNotAnInteger:
        applications = paginator.page(1)
    except EmptyPage:
        applications = paginator.page(paginator.num_pages)
    context = {
        'applications': applications,
    }
    return render(request, 'dashboard/applications.html', context)


class  ApplicationDetailView(LoginRequiredMixin, DetailView):
    model = Application
    template_name = 'dashboard/application-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payment'] = Payment.objects.filter(application=self.object)
        payments = Payment.objects.filter(application=self.object)
        context['total_payment'] = payments.aggregate(Sum('amount'))
        return context
    

class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'dashboard/application-form.html'


class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'dashboard/application-form.html'


class ApplicationDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Application

    def get_success_url(self):
        return reverse('applications')


@login_required
def application_search(request):
    query = request.GET['q']
    context = {
        'applications': Application.objects.filter(Q(full_name__icontains=query) | Q(file_number__iexact=query)),
    }
    return render(request, 'dashboard/application_search.html', context)


@login_required
def Payment_create(request, pk):
    payment_application = get_object_or_404(Application, id=pk)
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST, request.POST or None)
        if payment_form.is_valid():
            amount = request.POST.get('amount')
            application = payment_application
            payment = Payment.objects.create(application=application, amount=amount)
            payment.save()
            return redirect('applications')
    else:
        payment_form = PaymentForm()
    context = {
        'form':  payment_form,
    }
    return render(request, 'dashboard/payment-form.html', context)


class PaymentUpdateView(SuperUserRequiredMixin, UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'dashboard/payment-form.html'


class PaymentDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Payment

    def get_success_url(self):
        return reverse('applications')


@login_required
def dashboard(request):
    total_cases = Application.objects.all().count()
    approved_cases = Application.objects.filter(succeed='approved').count()
    rejected_cases = Application.objects.filter(succeed='rejected').count()
    inprocess_cases = Application.objects.filter(succeed='pending').count()
    total_leades = Lead.objects.all().count()
    approved_leades = Lead.objects.filter(succeed='approved').count()
    rejected_leades = Lead.objects.filter(succeed='rejected').count()
    inprocess_leades = Lead.objects.filter(succeed='pending').count()
    context = {
        'total_cases': total_cases,
        'approved_cases': approved_cases,
        'rejected_cases': rejected_cases,
        'inprocess_cases': inprocess_cases,
        'total_leades': total_leades,
        'approved_leades': approved_leades,
        'rejected_leades': rejected_leades,
        'inprocess_leades': inprocess_leades

    }
    return render(request, 'dashboard/dashboard.html', context)


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'dashboard/login.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')
