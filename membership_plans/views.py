from django.shortcuts import render

# Create your views here.


def membership_plans(request):

    """ A view that that renders the home page """

    return render(request, 'membership_plans/membership_plans.html')
