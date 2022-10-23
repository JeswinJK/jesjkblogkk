from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    path('must/',views.must),
    path('must/home',views.home),
    path('must/food',views.food),
    path('must/must',views.must),
    path('food/',views.food),
    path('food/home',views.home),
    path('food/must',views.must),
    path('food/food',views.food),
    path('register/',views.register),
    path('must/register',views.register),
    path('food/register',views.register),


]