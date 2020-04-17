from django.contrib import admin

# Register your models here.

from list.models import Item, UserIP
admin.site.register(Item)
admin.site.register(UserIP)
