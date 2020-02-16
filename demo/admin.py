from django.contrib import admin
from .models import Contact, Organization


class ConcatAdmin(admin.ModelAdmin):
    list_display = ("id", "deleted")

admin.site.register(Contact, ConcatAdmin)
admin.site.register(Organization)
