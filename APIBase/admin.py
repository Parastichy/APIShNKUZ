from django.contrib import admin

from .models import *


admin.site.register(ResourceRequirement)
admin.site.register(Resources)
admin.site.register(Unit)


@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ['searchCode', 'name']
    # list_filter = ['searchCode']
    search_fields = ['name']
