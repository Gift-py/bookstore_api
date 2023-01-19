from django.db import models

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
