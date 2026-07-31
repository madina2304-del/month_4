from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    pages = models.IntegerField()
    genre = models.CharField(max_length=100)
    published_date = models.DateField()
    image = models.ImageField(upload_to='books/')

    def __str__(self):
        return self.title
