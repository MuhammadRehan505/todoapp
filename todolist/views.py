from django.shortcuts import render, redirect
from .models import Todolist
from .forms import TodolistForm
from django.views.decorators.http import require_POST 
# Create your views here.

def index(request):
    todo_items = Todolist.objects.order_by('id')
    form = TodolistForm()
    context = {'my_data' : todo_items, 'hello_form' : form} 
    return render(request,'todolist/index.html', context)

@require_POST #WE want the form to this form here to be able to allow post.
def addTodoItem(request):    #that is name of my view addtodoitem.
    form = TodolistForm(request.POST)  #This is an instance of the form to capture data.POST is the method by which we capture the data.
    
    if form.is_valid():
        new_todo = Todolist(text=request.POST['shopping_items']) #inside we are going to cupture text data and we capture it from thte req.POST.
        new_todo.save() #that will save the new todo text that has been entered via the form.


    return redirect('index') #we are passing the index template code thats where we want to redirects.For use of this redirect first we import it.
 
def completedTodo(request, todo_id): #We are create the new function and this function is responsible for handling the items that have been marked as complete. inside request also the id of todo item.Every todo item will have a unique id in the database.
    todo = Todolist.objects.get(pk=todo_id) #we are going to acess the model which is todolist and grab the object from database. Because every item has unique id in database.
    todo.completed = True #which means that the item has been completed.
    todo.save()

    return redirect('index') #inside index is a template.


def deleteCompleted(request):
    Todolist.objects.filter(comeleted__exact=True).delete()         #We are querying all the objects in the database that have been marked as completed and the filter is going to search for exact values are set in database to true as completed then we call the delete method to remove them from database.
    
    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()

    return redirect('index')    
