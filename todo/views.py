from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem, PogChamp
from pog.champ import Pog

def todo_view(request):
    # c = TodoItem(content='permanent todo item C')
    # c.save()
    all_todo_items = TodoItem.objects.all()
    all_poggers = PogChamp.objects.all()
    print(all_todo_items)
    return render(request, 'todo.html',
                  {'all_items': all_todo_items,
                   'all_pogs': all_poggers})


def add_todo_view(request):
    # requests(gets) information from a given POST request. This is why you name it in the html input tag
    c = request.POST['content']
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def delete_todo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')


def add_pog_view(request):
    some_pogger = Pog('Kaz', 5)
    new_item = PogChamp(name=some_pogger.name, rank=some_pogger.rank)
    new_item.save()
    return HttpResponseRedirect('/todo/')


def delete_pog(request, pog_id):
    item_to_delete = PogChamp.objects.get(id=pog_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
