# urls.py
from django.conf import settings
from django.urls import path

from ami.settings import STATIC_URL
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('claims/', views.claims_view, name='claims'),
    path('inpatient/', views.inpatient_view, name='inpatient'),
    path('outpatient/', views.outpatient_view, name='outpatient'),
    path('logout/', views.logout_view, name='logout'),
    path('preauthorisation/', views.preauthorisation_view, name='preauthorisation'),
    path('capsbenefits/', views.capsbenefits_view, name='capsbenefits'),
]

