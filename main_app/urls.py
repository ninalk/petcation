from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('posts/', views.paths, name='posts'),
    path('accounts/signup/', views.signup, name='signup'),
    path('owners/', views.owners_index, name='owners_index'),
    path('owners/<int:owner_id>/', views.owners_detail, name='detail'),
    path('owners/create/', views.OwnerCreate.as_view(), name='owners_create'),
    path('owners/<int:pk>/update/', views.OwnerUpdate.as_view(), name='owners_update'),
    path('owners/<int:pk>/delete/', views.OwnerDelete.as_view(), name='owners_delete'),
    path('owners/<int:owner_id>/pet_create/', views.pets_create, name='pets_create'),
    path('owners/<int:owner_id>/add_pet/', views.add_pet, name='add_pet'),
    path('pets/<int:pet_id>/pet_update_form/', views.pets_update_form, name='pets_update_form'),
    path('pets/<int:pet_id>/pet_update/', views.pet_update, name='pets_update'),
    path('pets/<int:pet_id>/', views.pets_detail, name='pets_detail'),
    path('sitters/', views.sitters_index, name='sitters_index'),
    path('sitters/<int:sitter_id>/', views.sitters_detail, name='detail'),
    path('sitters/create/', views.SitterCreate.as_view(), name='sitters_create'),
    path('sitters/<int:pk>/update/', views.SitterUpdate.as_view(), name='sitters_update'),
    path('sitters/<int:pk>/delete/', views.SitterDelete.as_view(), name='sitters_delete'),
    path('sitters/<int:sitter_id>/add_photo/', views.add_photo, name='add_photo'),
 ]

