from django.conf.urls import url, include
from search_station import views

urlpatterns = [
    url(r'city$', views.search_train),
    url(r'stations$', views.stations),
]