from django.shortcuts import render


def index(request):
    """
    View function for the index page.

    This view renders the main index page of the website.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML of the index page.
    """
    return render(request, 'index.html')
