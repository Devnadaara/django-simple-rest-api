from django.db import models

# Create your models here.

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