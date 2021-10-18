from django.urls import path
from project.apps.api.v1.user import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('user/', views.User.as_view(), name='user'),
]