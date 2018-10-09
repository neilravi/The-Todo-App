from django import forms
from .models import TodoList

class TodoForm(forms.ModelForm):
	class Meta:
		model = TodoList
		fields = ['item', 'complated']
		widgets = {
			'item':forms.TextInput({"class":"form-control mr-sm-2", "placeholder":'Add New Item'}),
			'complated':forms.CheckboxInput({"class":"form-check-input position-static"})
		}
	
