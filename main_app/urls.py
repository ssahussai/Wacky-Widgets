from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('widget/create/', views.create_widget, name='create_widget'),
    path('widget/<int:pk>/delete/', views.RemoveWidget.as_view(), name='remove_widget'),
]