from django.db import models
# User model is already defined in Django we need to import 
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    # When user created product and user is deleted, 
    # value of user is null and product is not deleted
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True)
    # Image will be handled later
    # image =
    brand = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    rating = models.DecimalField(max_digits=7,decimal_places=2, null=True)
    numReviews = models.IntegerField(null=True, default=0)
    price = models.DecimalField(max_digits=7,decimal_places=2, null=True)
    countInStock = models.IntegerField(null=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    # By default django provide ID but we use _id in frontend 
    _id = models.AutoField(primary_key=True, editable=False)
