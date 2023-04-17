from django.db import models
from django.conf import settings

# Create your models here.


class Customer(models.Model):
    phone = models.CharField(max_length=255)
    birth_date = models.DateField()
    user= models.OneToOneField(settings.AUTH_USER_MODEL,models.CASCADE)


    def __str__(self) -> str:
        return f'{self.user.first_name}{self.user.last_name}'
    
    def first_name(self):
        return self.user.first_name
    
    def last_name(self):
        return self.user.last_name

class Collection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=255)
    description =models.TextField()
    inventory = models.IntegerField()
    collection = models.ForeignKey(Collection,on_delete=models.CASCADE,related_name='products')
    unit_price = models.PositiveIntegerField(default=0)


    def __str__(self) -> str:
        return self.title