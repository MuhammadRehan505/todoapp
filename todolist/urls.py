from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodoItem, name='add'),
    path('completed/<todo_id>', views.completedTodo, name='completed'), #we are going to do a slash then bcz we want to grab the id of the individual todo item so we are marking refrence that todo slash id and close.grab the complete and slash the actual id.
    path('deletecompleted', views.deleteCompleted, name='deletecompleted'),
    path('deleteall', views.deleteAll, name='deleteall')
]
