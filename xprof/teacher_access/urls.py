from django.urls import path, re_path
from django.contrib import admin

from . import views

urlpatterns = [

    path('auth/', views.log_page, name="authentication"),
    path('home/', views.home_page, name="home"),
    path('logout/', views.log_out, name="logout"),


    path('evaluate/', views.evaluate, name='evaluate'),
    path('evaluate/<course_slug>/', views.evaluate_course, name='evaluate_course'),


    path('new_course/', views.new_course, name='new_course'),


    path('courses/', views.all_courses, name='courses'),
    path('courses/<course_slug>', views.course_detail, name='course'),
    path('courses/<course_slug>/delete/', views.delete_course, name='delete_course'),
    path('courses/<course_slug>/edit/', views.edit_course, name='edit_course'),

    path('courses/<course_slug>/session/new_session/', views.new_session, name="new_session"),
    path('courses/<course_slug>/sessions/<session_slug>/delete/', views.delete_session, name="delete_session"),

    path('courses/<course_slug>/skills/new_skill/', views.new_skill, name="new_skill"),
    path('courses/<course_slug>/skills/<skill_slug>/', views.skill_detail, name="skill"),
    path('courses/<course_slug>/skills/<skill_slug>/delete/', views.delete_skill, name='delete_skill'),
    path('courses/<course_slug>/skills/<skill_slug>/edit/', views.edit_skill, name='edit_skill'),

]
