from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50,default="")
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="shop/images",default="")
    
    desc=models.CharField(max_length=300)
    publist_date=models.DateField()


    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=100,default="")
    phone=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=200,default="")

    def __str__(self):
        return self.name
    


class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    iems_json=models.CharField(max_length=500)
    name=models.CharField(max_length=90)
    amount=models.IntegerField(default=0)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    address2=models.CharField(max_length=111,default="")
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111)





class Item(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50,default="")
    img=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.name

class orderupdate(models.Model):
    updateid=models.AutoField(primary_key=True)
    orderid=models.IntegerField(default="")
    updatedesc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.updatedesc[0:10] + "..."