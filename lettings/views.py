from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """
    View function for the index page of lettings.

    This view retrieves all lettings from the database and passes them to the template for
    rendering.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML of the index page.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    View function for an individual letting page.

    This view retrieves a specific letting based on the provided letting_id and passes its
    details to the template for rendering.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to retrieve.

    Returns:
        HttpResponse: The rendered HTML of the letting detail page.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
