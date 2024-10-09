from django.contrib import admin

# Register your models here.
from .models import ToDoItem


class ToDoItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['task']}


admin.site.register(ToDoItem, ToDoItemAdmin)
