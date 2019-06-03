from django.urls import path, re_path

from . import views

urlpatterns = [
    path('auth/', views.log_page, name="authentication"),
    path('home/', views.home_page, name="home")
]
