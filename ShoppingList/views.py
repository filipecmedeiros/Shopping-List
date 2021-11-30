from django.shortcuts import render

from .models import Item


# Create your views here.
def item_list(request):
    itens = Item.objects.all()

    context = {
        'title':'Itens',
        'itens': itens
    }
    return render(request, 'itens_list.html', context)