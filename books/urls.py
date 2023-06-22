from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('scan/', views.scan_book, name='scan_book'),
    # Other URL patterns
    path('isbn_verify/', views.isbn_verify, name='isbn_verify'),
]

