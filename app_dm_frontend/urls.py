from django.urls import path
from . import views

app_name = 'app_dm_frontend'

urlpatterns = [
    path('', views.index, name='index'),
    path('maps/', views.maps, name='maps'),
    path('maps_detail/<str:name>/', views.maps_detail, name='maps_detail'),
    path('npc/', views.npc, name='npc'),
    path('diary/', views.diary, name='diary'),
    path('glem/', views.glem, name='glem'),
    path('notes/', views.notes, name='notes'),
    path('chronicle/', views.chronicle, name='chronicle'),
]