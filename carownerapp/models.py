from django.db import models

# Create your models here.
from django.db import models

class Country(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
        return str(self.name)
    
class City(models.Model):
  country = models.ForeignKey(
          Country, 
          on_delete=models.CASCADE
  )
  name = models.CharField(max_length=100)
  
  def __str__(self):
        return str(self.name)
    

class Teacher(models.Model):
  first_name = models.CharField(max_length=250)
  last_name = models.CharField(max_length=250)
  email = models.EmailField(max_length=250)
  
  def __str__(self):
        return str(self.first_name)
    
    
class Subject(models.Model):
  teachers = models.ManyToManyField(Teacher)
  title = models.CharField(max_length=250)
  
  def __str__(self):
        return str(self.title)
    

class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
   
    def __str__(self):
        return self.phone


class Employee(models.Model):
    first_name = models.CharField(max_length=100)

    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'