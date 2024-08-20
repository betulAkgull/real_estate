
from django.contrib import admin
from django.urls import path

from listings.views import listing_list, listings_retrieve, listing_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list, name='listing_list'),
    path('listings/<pk>/', listings_retrieve, name='listing_retrieve'),
    path('add-listing/', listing_create, name='listing_create')
]
