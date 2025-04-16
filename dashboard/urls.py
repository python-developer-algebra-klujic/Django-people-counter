from django.urls import path

from . import views


urlpatterns = [
    # http://www.domena.com/details/2
    path('details/<int:pk>', views.details, name='details'),
    path('', views.dashboard, name='dashboard'),
]