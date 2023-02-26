from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) #one customer one user. delete when user item is deleted
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(null= True, blank= True)

    def __str__(self):
        return self.name

    @property  #helps us access this as an attribute rather than a method
    def imageURL(self):
        try:
            url= self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, blank=True, null=True)#on del when customer is del we don't want to del order, set customer to null instead
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null= True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property  #helps us access this as an attribute rather than a method
    def get_cart_total(self):
        orderitems= self.orderitem_set.all()
        total= sum([item.get_total for item in orderitems]) #looping get toal to find the sum
        return total

    @property  #helps us access this as an attribute rather than a method
    def get_cart_items(self):
        orderitems= self.orderitem_set.all()
        total= sum([item.quantity for item in orderitems]) #looping quantity to find the sum
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete= models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property  #helps us access this as an attribute rather than a method
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, blank=True, null=True) #if customer gets del shipping add will still be there
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address