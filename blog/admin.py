from django.contrib import admin

# Register your models here.

from .models import visiter , contact, Blog

admin.site.register(visiter)
admin.site.register(contact)
admin.site.register(Blog)
