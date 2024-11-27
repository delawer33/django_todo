from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.ItemsView.as_view(), name='list'),
    path('create/', views.create_item, name='create'),
    path('archive/', views.archived_list, name='archive'),
    path('delete/<int:pk>', views.delete_item, name='delete'),
    path('mark_done/<int:pk>', views.mark_done, name='mark_done'),
]
