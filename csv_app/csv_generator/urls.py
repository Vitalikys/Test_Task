from django.urls import path, include
# from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('schemas/', SchemasView.as_view(), name='schemas'),
    # path('add_schema/', CreateSchema.as_view(), name='add_schema')
    path('add_schema/', create_schema, name='add_schema'),
    path('schema_del/<int:schema_id>/', delete_schema, name='del_schema'),
    path('<int:pk>/', SchemaDetailView.as_view(), name='detail_schema'),
    path('schema_edit/<int:schema_id>/', edit_schema, name='edit_schema'),
]
