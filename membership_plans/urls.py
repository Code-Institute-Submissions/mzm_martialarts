from django.urls import path
from . import views

urlpatterns = [
    path('membership_plans/', views.membership_plans, name='membership_plans')
]
