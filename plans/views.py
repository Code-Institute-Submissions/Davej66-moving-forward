from django.shortcuts import render


# Create your views here.


def plans(request):
    """ A view to return the index page """

    return render(request, 'plans/plans.html')
