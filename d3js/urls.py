from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.say_hello),
    path('record_visit/', views.record_visit, name='record_visit'),
    path('recent_visit_count/', views.recent_visit_count, name='recent_visit_count'),
]
