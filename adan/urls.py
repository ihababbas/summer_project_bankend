# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('adan/', views.scrape_data, name='scrape_data'),
]