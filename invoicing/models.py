from django.db import models

# Create your models here.
class Employee(models.Model):
  first_name= models.CharField(max_length= 100)
  last_name = models.CharField(max_length= 100)
  email     = models.EmailField()

  def __str__(self):
    return self.first_name + ' ' + self.last_name


class Vendor(models.Model):
  vendor_num = models.CharField(max_length= 100)
  vendor_name= models.CharField(max_length= 150)

  def __str__(self):
    return self.vendor_name
    

class Invoice(models.Model):
  invoice_num= models.CharField(max_length= 100)
  vendor = models.ForeignKey(Vendor, on_delete= models.CASCADE)
  invoice_date  = models.DateField()
  invoice_amount= models.DecimalField(max_digits= 15, decimal_places= 2)
  description   = models.TextField()

  def __str__(self):
    return self.vendor.vendor_name + ' ' + self.invoice_num
