from email import message
from django.db import models

# Create your models here.
CHOICE = (
    ("one","Kursatilsin"),
    ("two","Kursatilmasin")
)

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/img')
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    status = models.CharFieMld(max_length=14,
                choices=CHOICE,
                default="one")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title

class Commints(models.Model):
    name = models.Model.Chrfiled(max_length=100)
    email = models.Model.Emailfiled(max_length=254)