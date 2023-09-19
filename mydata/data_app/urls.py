from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload-media/', views.upload_media, name='upload_media'),
    path('create-start-point/', views.create_start_point, name='create_start_point'),
    path('create-end-point/', views.create_end_point, name='create_end_point'),
    path('success-page/', views.success_page, name='success_page'),
]
