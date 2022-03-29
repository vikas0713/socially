
from django.urls import path

from timeline import views


urlpatterns = [
    path('', views.index),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

]
