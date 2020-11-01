from django.urls import path

from . import views

urlpatterns = [
    path('create_task/', views.TaskCreateView.as_view(), name='create_task'),
    path('detail_<int:pk>/', views.CityDetailView.as_view(), name='main_detail'),
    path('', views.CityListView.as_view(), name='main'),
]
