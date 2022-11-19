from django.db import models


# Create your models here.
class Registration(models.Model):
    zip = models.CharField('Zip Code',max_length=6,null=False,default="")
    district=models.CharField('District',max_length=25,null=False,default="")
    owner = models.CharField('Owner Name', max_length=20, null=False)
    price = models.CharField('Price', max_length=20, null=False, default="")
    address = models.CharField('Location', max_length=100, null=False, default="")
    about = models.CharField('Description', blank=False, max_length=200, default="")
    phone_no = models.CharField('Phone number', max_length=10, blank=False, default="")

    def __str__(self):
        return self.price + ' ' + self.owner


class Login(models.Model):
    username = models.CharField('User name', max_length=20, null=False)
    password = models.CharField('Password', max_length=20, null=False)
    cpass = models.CharField('Confirm password', max_length=20, null=False)

    def __str__(self):
        return self.username
