from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import RouteDs


class RoutedsListView(ListView):
    model = RouteDs
    template_name = 'home.html'


class RoutedsDetailView(LoginRequiredMixin, DetailView):
    model = RouteDs
    login_url = 'login'
    template_name = 'routeds_detail.html'


class RoutedsUpdateView(LoginRequiredMixin, UpdateView):
    model = RouteDs
    login_url = 'login'
    fields = ('rd', 'tec', 'eventum', 'client', 'numline')
    template_name = 'routeds_update.html'
    success_url = reverse_lazy('home')


class RoutedsCreateView(LoginRequiredMixin, CreateView):
    model = RouteDs
    login_url = 'login'
    fields = ('rd', 'tec', 'eventum', 'client', 'numline')
    template_name = 'routeds_new.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RoutedsDeleteView(LoginRequiredMixin, DeleteView):
    model = RouteDs
    login_url = 'login'
    template_name = 'routeds_detele.html'
    success_url = reverse_lazy('home')
