from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_data/', views.all_data, name='all_data'),
    path('upload-media/', views.upload_media, name='upload_media'),
    path('create-start-point/', views.create_start_point, name='create_start_point'),
    path('create-end-point/', views.create_end_point, name='create_end_point'),
    path('success-page/', views.success_page, name='success_page'),
    path('submit_data/', views.submit_data, name='submit_data'),
    path('user_data/<int:user_id>/', views.user_data, name='user_data'),
]
