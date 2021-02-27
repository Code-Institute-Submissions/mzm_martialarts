from django.shortcuts import render
from djstripe.models import Product

# Create your views here.


def membership_plans(request):

    """ A view that that renders the membership page """

    return render(request, 'membership_plans.html', {
        'products': Product.objects.all()
    })
