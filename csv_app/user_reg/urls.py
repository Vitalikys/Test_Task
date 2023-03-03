from django.urls import path, include
# from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('login/', user_login, name='login_url'),
    path('logout/', logout_view, name='logout_url'),
    # path('accounts/login/',
    #      auth_views.LoginView.as_view(template_name='login.html',
    #                                   redirect_authenticated_user=True),
    #      name='login_url'),
]
