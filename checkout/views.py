from django.shortcuts import render

# Create your views here.


def view_checkout(request):

    """ A view that that renders the checkout page """

    return render(request, '/checkout/checkout.html')
