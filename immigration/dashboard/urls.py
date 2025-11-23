from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('leades/', views.LeadsListView.as_view(), name='leads'),
    path('branch-leades/<int:pk>/', views.leads_by_banch, name='branch-leads'),
    path('lead/<int:pk>/', views.LeadDetailView.as_view(), name='lead-details'),
    path('new-lead/', views.LeadCreateView.as_view(), name='new-lead'),
    path('edit-lead/<int:pk>/', views.LeadUpdateView.as_view(), name='edit-lead'),
    path('delete-lead/<int:pk>/', views.LeadDeleteView.as_view(), name='delete-lead'),
    path('applications/', views.ApplicationsListView.as_view(), name='applications'),
    path('branch-applications/<int:pk>/', views.applications_by_banch, name='branch-applications'),
    path('application/<int:pk>/', views.ApplicationDetailView.as_view(), name='application-details'),
    path('new-application/', views.ApplicationCreateView.as_view(), name='new-application'),
    path('edit-application/<int:pk>/', views.ApplicationUpdateView.as_view(), name='edit-application'),
    path('delete-application/<int:pk>/', views.ApplicationDeleteView.as_view(), name='delete-application'),
    path('payment/<int:pk>/add/', views.Payment_create, name='add-payment'),
    path('payment/<int:pk>/edit/', views.PaymentUpdateView.as_view(), name='edit-payment'),
    path('payment/<int:pk>/delete/', views.PaymentDeleteView.as_view(), name='delete-payment'),
    path('application-search/', views.application_search, name='application-search'),
    path('lead-search/', views.lead_search, name='lead-search'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='dashboard/logout.html'), name='logout'),
]
