from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('home/', views.todoHome, name='home'),
    path('delete/<int:id>/', views.delItem, name='delete'),
    path('update/<int:id>/', views.itemUpdate, name='update'),
    path('another/update/<int:id>/', views.itemUpdate, name='another-update'),
    path('item/cross-off/<int:id>/', views.crossOff, name='cross-off'),
    path('item/uncross/<int:id>/', views.unCross, name='uncross'),
]