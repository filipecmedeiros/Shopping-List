from .models import ShoppingList, Item
import logging

class Command(object):

    def process(self, text):
        words = text.lower().split(' ')

        if words[1] == 'lista':
            if self.add(words[0]):
                self.add_list(words[2])


    def add(self, word):
        possibilities = ['adicionar', 'criar']
        return word in possibilities

    def remove(self, word):
        possibilities = ['remover', 'deletar', 'apagar']
        return word in possibilities

    def activate(self, word):
        possibilities = ['ativar']
        return word in possibilities

    def activate(self, word):
        possibilities = ['desativar']
        return word in possibilities

    def add_list(self, name):
        logging.warning(name)
        ShoppingList.objects.create(name=name, active=True)
    