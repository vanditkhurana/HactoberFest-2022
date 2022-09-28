from django.db import models

# Create your models here.
class Author(models.Model):
    pass
class Book(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, blank=True)
    author = models.ManyToManyField(Author, blank=True)
    date_of_publication = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    slug  = models.SlugField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    pass
   