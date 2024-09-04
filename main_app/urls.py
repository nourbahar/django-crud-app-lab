from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.car_index, name='car-index'),
    path('cars/<int:car_id>/', views.car_detail, name='car-detail'),
    path('cars/create/', views.CarCreate.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'),
    path(
        'cars/<int:car_id>/add-service/', 
        views.add_service, 
        name='add-service'
    ),
    path('accounts/signup/', views.signup, name='signup')
   
]



