from django.contrib import admin

# Register your models here.
from .models import ShoppingList, Item

class ShoppingListAdmin (admin.ModelAdmin):
    list_display = ['name', 'active']
    search_display = ['name', 'active']
    search_fields = ['name', 'active']

admin.site.register(ShoppingList, ShoppingListAdmin)


class ItemAdmin (admin.ModelAdmin):
	list_display = ['name', 'shopping_list']
	list_filter = ['shopping_list']
	search_display = ['shopping_list__name', 'name']
	search_fields = ['shopping_list__name', 'name']

admin.site.register(Item, ItemAdmin)
