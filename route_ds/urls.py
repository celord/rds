from django.urls import path
from .views import (RoutedsListView,
                    RoutedsUpdateView,
                    RoutedsDetailView,
                    RoutedsDeleteView,
                    RoutedsCreateView)

urlpatterns = [
    path('', RoutedsListView.as_view(), name='home'),
    path('new/', RoutedsCreateView.as_view(), name='create'),
    path('<int:pk>/edit/',RoutedsUpdateView.as_view(), name='routeds_edit'),
    path('<int:pk>/', RoutedsDetailView.as_view(), name='routeds_detail'),
    path('<int:pk>/delete/', RoutedsDeleteView.as_view(), name='routeds_detail'),
    
]
