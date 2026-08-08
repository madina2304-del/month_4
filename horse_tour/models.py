from django.db import models


class Horse(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class HorseCategory(models.Model):
    name = models.CharField(max_length=100)
    horses = models.ManyToManyField(Horse)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    horses = models.ManyToManyField(Horse)

    def __str__(self):
        return self.name

class Booking(models.Model):
    person_name = models.CharField(max_length=50)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)  
  

    def __str__(self):
        return self.person_name

class Comment(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.author    

