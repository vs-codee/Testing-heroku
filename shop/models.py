from django.db import models

# Create your models here.
class Products(models.Model):
    product_id=models.AutoField
    product_name=models.CharField( max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField( max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField( max_length=300)
    pub_date=models.DateTimeField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
    class Meta:
        verbose_name_plural = "Products"

class Contacts(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField( max_length=50)
    email=models.CharField(max_length=100,default="")
    phone=models.CharField( max_length=20,default="")
    desc=models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contacts"

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    json=models.CharField(max_length=5000)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Orders"

class OrderUpdate(models.Model):

    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=600)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc

    
