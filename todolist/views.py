from django.shortcuts import render
from .models import Todolist
# Create your views here.

def index(request):
    todo_items = Todolist.objects.order_by('id')
    context = {'my_data' : todo_items}
    return render(request,'todolist/index.html', context)