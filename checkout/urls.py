from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_checkout, name='view_checkout'),
    path('stripe/', include('djstripe.urls', namespace="djstripe")),
    path('create-sub/', views.create_sub, name='create sub'),
    path('complete/', views.complete, name='complete'),
]
