from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    
    path('login/', views.login_view, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='Logout'),
    path('userDelete/<int:pk>', views.UserDelete.as_view(), name='UserDelete'),
    path('editProfile/', views.editProfile, name="EditProfile"),
    path('agregarAvatar/', views.addAvatar, name="AddAvatar"),
    
]