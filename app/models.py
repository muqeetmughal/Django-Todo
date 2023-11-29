from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=150, null=True, blank= True)
    detail = models.TextField(max_length=150, null=True, blank= True)