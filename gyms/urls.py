from django.urls import path
from gyms import views

urlpatterns = [
    
    # Vista Basada en CLASS 
    path('gymList/', views.GymList.as_view() , name='GymList'),
    path('gymCreate/', views.GymCreate.as_view() , name='GymCreate'),
    path('gymUpdate/<int:pk>', views.GymUpdate.as_view() , name='GymUpdate'),
    path('gymDelete/<int:pk>', views.GymDelete.as_view() , name='GymDelete'),
    path('gymDetail/<int:pk>', views.GymDetail.as_view(), name='GymDetail'),
    
]