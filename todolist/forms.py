from django import forms

class TodolistForm(forms.Form):
    shopping_items = forms.CharField(max_length=45,widget=forms.TextInput(
           attrs={'placeholder' : 'Enter todo e.g Grocery Shopping', 'aria-label' : 'Todo', 'aria-describeby': 'add-btn'}))
