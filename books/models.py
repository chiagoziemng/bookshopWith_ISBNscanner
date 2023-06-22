from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField()
    edition = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    language = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13, unique=True)
    image = models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return self.title
