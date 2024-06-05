from django.urls import path
from . import views

urlpatterns = [
  path('about/', views.about, name='about'),
  path('cars/', views.car_index, name='car-index'),
  path('cars/<int:car_id>/', views.car_detail, name='car-detail'),
  path('cars/create/', views.CarCreate.as_view(), name='car-create'),
  path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car-update'),
  path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'),
  path('cars/<int:car_id>/add-service/', views.add_service, name='add-service'),
  path('cars/<int:car_id>/assoc-mod/<int:mod_id>/', views.assoc_mod, name='assoc-mod'),
  path('mods/create/', views.ModCreate.as_view(), name='mod-create'),
  path('mods/<int:pk>/', views.ModDetail.as_view(), name='mod-detail'),
  path('mods/', views.ModList.as_view(), name='mod-index'),
  path('mods/<int:pk>/update/', views.ModUpdate.as_view(), name='mod-update'),
  path('toys/<int:pk>/delete/', views.ModDelete.as_view(), name='mod-delete'),
  path('', views.Home.as_view(), name='home'),
  path('accounts/signup/', views.signup, name='signup'),
]