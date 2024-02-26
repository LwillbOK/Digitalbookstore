#from django.contrib.auth.models import Author
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    works = models.TextField()
    contact = models.CharField(max_length=100)

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    description = models.TextField()
    pub_date = models.DateField('Publish date')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title



