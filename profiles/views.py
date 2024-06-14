from django.shortcuts import render
from profiles.models import Profile


def index(request):
    """
    View function for the index page of profiles.

    This view retrieves all profiles from the database and passes them to the template
    for rendering.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML of the index page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    View function for an individual profile page.

    This view retrieves a specific profile based on the provided username and passes
    its details to the template for rendering.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile to retrieve.

    Returns:
        HttpResponse: The rendered HTML of the profile detail page.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
