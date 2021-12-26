from django.contrib import admin
from task.models import Category,TodoTask
# Register your models here.
admin.site.register(Category)
admin.site.register(TodoTask)