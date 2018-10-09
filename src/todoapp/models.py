from django.db import models

# Create your models here.

class TodoList(models.Model):
	item = models.CharField(max_length=200)
	complated = models.BooleanField(default=False)

	def __str__(self):
		return self.item + ' | ' +str(self.complated)

		