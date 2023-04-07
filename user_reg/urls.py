from django.urls import path, include
# from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('login/', user_login, name='login_url'),
    path('logout/', logout_view, name='logout_url'),

]
