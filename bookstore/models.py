from django.db import models
from uuid import uuid4

class Book(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, unique= True, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title, self.author, self.book, self.id_book
# Create your models here.
