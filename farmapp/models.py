from distutils.command.upload import upload
from email.policy import default
from django.db import models


class Login(models.Model):
    uname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
class Registration (models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=300,default="test")
class Addcropdetails (models.Model):
    id=models.AutoField(primary_key=True)
    fid=models.ForeignKey(Registration,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=100)
    qty=models.IntegerField(default=0)
    status=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
class Addnews (models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    news=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
class Feedback (models.Model):
    id=models.AutoField(primary_key=True)
    fid=models.ForeignKey(Registration,on_delete=models.CASCADE,blank=True,null=True)
    Feedbacks=models.CharField(max_length=100)
    
class Loantype (models.Model):
    id=models.AutoField(primary_key=True)
    type=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
class Loanrequest (models.Model):
    id=models.AutoField(primary_key=True)
    loanid=models.ForeignKey(Loantype,on_delete=models.CASCADE,blank=True,null=True)
    uid=models.ForeignKey(Registration,on_delete=models.CASCADE,blank=True,null=True)
    requestamount=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
class delivaryboy (models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
class delivary (models.Model):
    id=models.AutoField(primary_key=True)
    did=models.ForeignKey(delivaryboy,on_delete=models.CASCADE,blank=True,null=True)
    cropid=models.ForeignKey(Addcropdetails,on_delete=models.CASCADE,blank=True,null=True)
    amount=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
       