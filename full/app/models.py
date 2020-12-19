from django.db import models

# Create your models here.
class Student(models.Model):
    c=(
        ("M","Male"),("F","Female")
    )
    name=models.CharField(max_length=50)
    email=models.EmailField()
    roll_no=models.IntegerField(unique=True)
    fee=models.FloatField()
    gender=models.CharField(max_length=50,choices=c)
    address=models.TextField()
    is_registered=models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name



class Contact_Us(models.Model):
    name=models.CharField(max_length=50)
    contact_number=models.IntegerField(blank=True,unique=True)        
    subject=models.CharField(max_length=50)
    message =models.TextField()
    added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Contact_Us"  


class Category(models.Model):
    name=models.CharField(max_length=50)
    cover_pic=models.FileField(upload_to="media/%Y%M%D")
    description=models.TextField()
    added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name        

