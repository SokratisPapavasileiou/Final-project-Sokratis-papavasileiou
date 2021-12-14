from django.db import models
from django.conf import settings
import os
# Create your models here.
class test(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f":{self.name}"

class test2(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f":{self.name}"
def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'img')
class menu(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    img= models.ImageField( upload_to="img",null=True,blank=True)

    
      
    def __str__(self):
        return f":{self.name}:{self.description}"
            

class userdata(models.Model):
  
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    password=models.CharField(max_length=50)
    

    
    def __str__(self):
        return f":{self.name}:{self.email}:{self.password}"
class userating(models.Model):
    Rating_CHOICES = (
    (1, 'Poor service'),
    (2, 'Average service'),
    (3, 'Good service'),
    (4, 'Very Good service'),
    (5, 'Excellent service')
    )
    
    rating=models.IntegerField(choices=Rating_CHOICES, default=1)

    
    def __str__(self):
        return f":{self.rating}"