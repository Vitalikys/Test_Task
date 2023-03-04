from django.urls import path, include
# from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('schemas/', SchemasView.as_view(), name='schemas'),
    # path('add_schema/', CreateSchema.as_view(), name='add_schema')
    path('add_schema/', create_schema, name='add_schema')

]
