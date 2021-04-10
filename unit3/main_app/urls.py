from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wackywidget/create/', views.WidgetCreate.as_view(), name='widgets_create'),
    path('wackywidget/<int:pk>/delete', views.DeleteWidget, name='delete'),
]
