from django.db import models

# Create your models here.

class Product(models.Model):
    pid = models.IntegerField(unique=True)
    pname = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    price = models.IntegerField()
    stock_qty = models.IntegerField()
    brand = models.CharField(max_length=50)
    supplier = models.CharField(max_length=50)
    purchase_date = models.DateField()
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.pid}, {self.pname}, {self.price}"

