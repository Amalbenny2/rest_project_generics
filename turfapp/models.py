
from django.db import models

# Create your models here.
class venue (models.Model):
    name=models.CharField(max_length=34,unique=True)
    datetime=models.DateTimeField(null=True)

class customers(models.Model):
    name=models.CharField(max_length=40)
    address=models.TextField()
    phone_number=models.IntegerField()
    datetime=models.DateTimeField(unique=True,null=True)
    Venue=models.ForeignKey(venue,on_delete=models.CASCADE,null=True)




    