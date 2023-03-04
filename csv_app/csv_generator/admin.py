from django.contrib import admin

from .models import *


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    fields = ('name', 'user', 'full_name', 'string_character')
    list_display = ('name', 'user')

admin.register(SchemaAdmin)
