from django.urls import path
from crudapp import views

urlpatterns = [  
    path('', views.read),
    path('view/<str:pk>/', views.view),
    path('create/', views.create),
    path('update/<str:pk>/', views.Update),
    path('delete/<str:pk>/', views.abort),
]