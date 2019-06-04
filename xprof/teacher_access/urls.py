from django.urls import path, re_path

from . import views

urlpatterns = [
    path('auth/', views.log_page, name="authentication"),
    path('register/', views.new_user, name="register"),
    path('home/', views.home_page, name="home"),
    path('logout/', views.log_out, name="logout"),
]
