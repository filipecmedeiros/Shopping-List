from django.shortcuts import render
from .models import Item
import json
from .Command import Command
import logging

# Create your views here.
def item_list(request):
    if request.method == 'GET':
        itens = Item.objects.all()

        context = {
            'title':'Itens',
            'itens': itens
        }
        return render(request, 'itens_list.html', context)
    else:
        command = Command()
        data = json.loads(request.body)
        text = data['text']
        logging.warning(text)

        command.process(text)
        context = {
            'title': text
        }
        return render(request, 'itens_list.html', context)


