from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view_items'),
    path('login/', views.login, name='login'),
    path('getInTouch/', views.SaveFeedback, name='feedback'),
    path('findComments/', views.findComment, name='feedback'),

]
