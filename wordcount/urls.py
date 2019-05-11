from . import view
from django.urls import path

urlpatterns = [
path('',view.home,name='homepage'),
path('count/',view.count,name='counttext'),
path('about/',view.about,name='aboutauther')
]
