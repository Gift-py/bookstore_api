from django.db import models

class Author(models.Model):
    author_id = models.IntegerField(primary_key=True, default=1, blank=False, null=False)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.IntegerField(primary_key=True, default=1, blank=False, null=False)
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
