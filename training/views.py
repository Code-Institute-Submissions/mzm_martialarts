from django.shortcuts import render

# Create your views here.


def training(request):

    """ A view that that renders the training page """

    return render(request, 'training/training.html')
