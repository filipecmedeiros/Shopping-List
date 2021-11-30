from django.contrib import admin

# Register your models here.
from .models import ShoppingList, Item

class ShoppingListAdmin (admin.ModelAdmin):
    list_display = ['name', 'user']
    list_filter = ['user']
    search_display = ['user', 'name']
    search_fields = ['user__first_name', 'user__last_name', 'user__username', 'name']

admin.site.register(ShoppingList, ShoppingListAdmin)


class ItemAdmin (admin.ModelAdmin):
	list_display = ['name', 'shopping_list']
	list_filter = ['shopping_list']
	search_display = ['shopping_list__name', 'name']
	search_fields = ['shopping_list__name', 'name']

admin.site.register(Item, ItemAdmin)
