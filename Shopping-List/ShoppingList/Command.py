from .models import ShoppingList, Item
import logging


ADD = ['adicionar', 'criar']
DELETE = ['remover', 'deletar', 'apagar']
ACTIVATE = ['ativar']
DEACTIVATE = ['desativar']


class Command(object):

    def process(self, text):
        words = text.lower().split(' ')
        stopwords = ['na', 'de', 'da']
        words = [word for word in words if word not in stopwords]
        logging.warning(words)

        operation = words[0]
        
        if words[1] == 'lista':
            name = words[2]
            
            logging.warning(operation)
            logging.warning(name)

            if operation in ADD:
                self.add_list(name)
            elif operation in DELETE:
                self.delete_list(name)
            elif operation in ACTIVATE:
                self.activate_list(name)
            elif operation in DEACTIVATE:
                self.deactivate_list(name)
        
        elif words[1] == 'item':
            item_name = words[2]

            if words[3] == 'lista':
                list_name = words[4]
            
            logging.warning(operation)
            logging.warning(item_name)
            logging.warning(list_name)

            if operation in ADD:
                self.add_item(item_name, list_name)
            elif operation in DELETE:
                self.delete_item(item_name, list_name)
        else:
            item_name = words[1]

            if words[2] == 'lista':
                list_name = words[3]
            
            logging.warning(operation)
            logging.warning(item_name)
            logging.warning(list_name)

            if operation in ADD:
                self.add_item(item_name, list_name)
            elif operation in DELETE:
                self.delete_item(item_name, list_name)

    def add_list(self, name):
        ShoppingList.objects.create(name=name, active=True)
    
    def delete_list(self, name):
        ShoppingList.objects.filter(name=name).delete()

    def activate_list(self, name):
        ShoppingList.objects.filter(name=name).update(active=True)

    def deactivate_list(self, name):
        ShoppingList.objects.filter(name=name).update(active=False)

    # Item
    def get_list(self, list_name):
        return ShoppingList.objects.filter(name=list_name).first()

    def add_item(self, item_name, list_name):
        Item.objects.create(name=item_name, shopping_list=self.get_list(list_name))
    
    def delete_item(self, item_name, list_name):
        Item.objects.filter(name=item_name, shopping_list=self.get_list(list_name)).delete()

