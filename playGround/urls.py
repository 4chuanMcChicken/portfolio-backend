from django.urls import path
from . import views

urlpatterns = [
    path("showCases/", views.get_show_cases)
]
