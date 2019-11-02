from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path(r'rsvp', views.rsvp, name='rsvp'),
    # path(r'rsvp/', views.rsvp, name='rsvp'),
    path(r'thanks', views.thanks, name='thanks'),
    path(r'thanks/', views.thanks, name='thanks'),
    path(r'need_help', views.need_help, name='need_help'),
    path(r'need_help/', views.need_help, name='need_help'),
]
