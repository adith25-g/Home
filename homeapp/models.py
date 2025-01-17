from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES=(
    ('door','Doors'),
    ('window','Windows'),
    ('furnicher','Furnichers'),
    ('textile','Textiles'),
    ('light','Lightings'),
    ('kichen','Kichen Accessories'),
    ('bathroom','Bathroom Accessories'),
    ('wall','Wall Decor'),
)

class Product(models.Model):
    title=models.CharField(max_length=200)
    selling_price=models.FloatField()
    description=models.TextField()
   
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=10)
    product_image=models.ImageField(upload_to='product')
    
    def __str__ (self):
        return self.title

class Customer(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   name = models.CharField(max_length=200)
   locality = models.CharField(max_length=200)
   city = models.CharField(max_length=50)
   mobile = models.IntegerField(default=0)
   pincode=models.IntegerField()
   def __str__(self):
        return self.name
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity*self.product.selling_price



class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True)
    paid = models.BooleanField(default=False)
