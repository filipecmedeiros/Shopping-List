from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class ShoppingList (models.Model):
    name = models.CharField('Nome', max_length=255, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')

    created = models.DateTimeField('Criado', auto_now_add=True)
    modified = models.DateTimeField('Modificado', auto_now=True)

    class Meta:
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'
        ordering = ['id', 'name']

    def __str__(self):
        return self.name

class Item (models.Model):

    name = models.CharField('Nome', max_length=100, unique=True)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, null=False, verbose_name='Lista')

    created = models.DateTimeField('Criado', auto_now_add=True)
    modified = models.DateTimeField('Modificado', auto_now=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        ordering = ['shopping_list', 'id', 'name']

    def __str__(self):
        return str(self.id) + '. ' + self.name

