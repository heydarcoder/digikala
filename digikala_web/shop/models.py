from datetime import datetime

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200 , default="" ,blank=True , null=True )
    price = models.DecimalField(default=0 , decimal_places= 0, max_digits= 12)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default=1)
    picture = models.ImageField(upload_to="upload/products/")
    SIZES = (
        ('M','32'),
        ('L','64'),
        ('X','128'),
    )
    size = models.CharField(max_length=1, choices=SIZES, default='32')

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200 , default="" ,blank=True , null=True )
    phone = models.CharField(max_length=20 , blank=True , null=True )
    email = models.EmailField()
    date = models.DateTimeField(default=datetime.today())
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.customer} {self.product} {self.quantity}"





