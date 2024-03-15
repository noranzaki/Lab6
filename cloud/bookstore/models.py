from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='bookstore/images/', null=True)
    author = models.CharField(max_length=100)
    price = models.IntegerField(default=10, null=True)
    numpages = models.IntegerField(default=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True, null=True) #update
    def __str__(self):
        return f"{self.name}"
    @property
    def image_url(self):
        return f'/media/{self.image}'