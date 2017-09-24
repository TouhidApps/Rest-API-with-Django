from django.contrib import admin
from .models import Item


# Register your models here. touhid1010@gmail.com 12345678t

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount']

admin.site.register(Item, ItemAdmin)
