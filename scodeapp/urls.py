#app level urls
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio_details1', views.portfolio, name='portfolio_details1'),
    path('portfolio_details2', views.portfolio_2, name='portfolio_details2'),#template name
    path('portfolio_details3', views.portfolio_3, name='portfolio_details3'),
    path('portfolio_details4', views.portfolio_4, name='portfolio_details4'),
    path('portfolio_details5', views.portfolio_5, name='portfolio_details5'),
    path('portfolio_details6', views.portfolio_6, name='portfolio_details6'),
    
]
