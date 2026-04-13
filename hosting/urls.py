from django.urls import path
from . import views

app_name = 'hosting'
urlpatterns = [
    # Domain URLs
    path('domains/', views.domain_list, name='domain_list'),
    path('domains/create/', views.domain_create, name='domain_create'),
    path('domains/update/<int:pk>/', views.domain_update, name='domain_update'),
    path('domains/delete/<int:pk>/', views.domain_delete, name='domain_delete'),

    # Server URLs
    path('servers/', views.server_list, name='server_list'),
    path('servers/create/', views.server_create, name='server_create'),
    path('servers/update/<int:pk>/', views.server_update, name='server_update'),
    path('servers/delete/<int:pk>/', views.server_delete, name='server_delete'),
]