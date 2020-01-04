from django.urls import path
from list import views

app_name = 'list'

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('mark/<str:pk>/', views.mark, name='mark'),
]
