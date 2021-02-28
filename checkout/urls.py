from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('stripe/', include('djstripe.urls', namespace="djstripe")),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('webhook/', views.stripe_webhook),
]
