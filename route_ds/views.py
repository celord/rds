from django.views.generic import ListView

from .models import RouteDs

class RoutedsListView(ListView):
    model = RouteDs
    template_name = 'home.html'
