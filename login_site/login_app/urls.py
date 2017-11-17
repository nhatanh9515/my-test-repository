from django.conf.urls import url
from login_app import views

app_name = 'login_app'

urlpatterns = [
    url(r'^login/', views.user_login, name='login'),
    url(r'^register/', views.user_register, name='register'),
    url(r'^index/', views.index, name='index'),
]
