from django.contrib import admin
from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'detail']  # Specify the fields you want to display in the admin list view

# Register the ToDo model with the custom admin options
admin.site.register(ToDo, ToDoAdmin)
