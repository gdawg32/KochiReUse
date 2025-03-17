from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.listings_view, name='listings'),  # New view for initial page load
    path('search_listings/', views.search_listings, name='search_listings'),  # Existing HTMX endpoint
    path('filter_listings/', views.filter_listings, name='filter_listings'),  # Existing HTMX endpoint
    path('sort_listings/', views.sort_listings, name='sort_listings'),  # Existing HTMX endpoint
] 