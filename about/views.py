from django.shortcuts import render

# Create your views here.


def about(request):

    """ A view that that renders the about page """

    return render(request, 'about/about.html')
