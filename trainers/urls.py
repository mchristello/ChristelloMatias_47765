from django.urls import path
from trainers import views

urlpatterns = [
    
    path('', views.views_trainer, name='Trainer'),
    
    # Vista Basada en CLASS 
    path('trainerList/', views.TrainerList.as_view() , name='TrainerList'),
    path('trainerCreate/', views.TrainerCreate.as_view() , name='TrainerCreate'),
    path('trainerUpdate/<int:pk>', views.TrainerUpdate.as_view() , name='TrainerUpdate'),
    path('trainerDelete/<int:pk>', views.TrainerDelete.as_view() , name='TrainerDelete'),
    path('trainerDetail/<int:pk>', views.TrainerDetail.as_view(), name='TrainerDetail'),
    
    
]