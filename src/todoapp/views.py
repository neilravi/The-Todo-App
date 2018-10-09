from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList
from .forms import TodoForm
from django.contrib import messages
# Create your views here.

def todoHome(request):
	if request.method == 'POST':
		form = TodoForm(request.POST or None)

		if form.is_valid():
			form.save()
			print(form.cleaned_data)	
			all_item = TodoList.objects.all()
			messages.success(request, ('Item has been added to the list.'))
			return render(request, 'todoapp/home.html',{'all_item':all_item, 'form':form})	
	else:
		form = TodoForm()
		all_item = TodoList.objects.all()
		return render(request, 'todoapp/home.html', {'all_item':all_item, 'form':form})

def itemUpdate(request, id=None):
	instance = get_object_or_404(TodoList, id=id)
	form = TodoForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		messages.info(request, ('item updated.'))
		return redirect('todoapp:home')	
	return render(request, 'todoapp/item_update.html', {'form':form})


def anotherUpdate(request, id=None):
	instance = get_object_or_404(TodoList, id=id)
	form = TodoForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		messages.info(request, ('item updated.'))
		return redirect('todoapp:home')	
	return render(request, 'todoapp/edit.html')			



def delItem(request, id=None):
	item = get_object_or_404(TodoList, id=id)
	if item:
		item.delete()
		messages.info(request, ('item deleted.'))
		return redirect('todoapp:home')


def crossOff(request, id=None):
	item = get_object_or_404(TodoList, id=id)
	if item:
		item.complated = True
		item.save()
		return redirect('todoapp:home')


def unCross(request, id):
	item = get_object_or_404(TodoList, id=id)
	if item:
		item.complated = False
		item.save()
		return redirect('todoapp:home')