from django.urls import path
from .views import RoutedsListView

urlpatterns = [
    path('', RoutedsListView.as_view(), name='home')
]
