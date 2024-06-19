from django.contrib import admin
from .models import all_items, users

admin.site.register(all_items)
admin.site.register(users)
