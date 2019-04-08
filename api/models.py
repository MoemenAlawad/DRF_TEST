from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=30)   
    def __str__(self):
        return self.name       
class UserBooking(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    service = models.ForeignKey(Service,on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status_choices =  (
        ('Available', 'Available'),
        ('Not available', 'Not available'),
        )
    status = models.CharField(max_length=50,choices=status_choices,default="AVAILABLE")
    def __str__(self):
        return "name:{} ,phone:{} ,email:{} ,service:{} ,start_date:{} ,end_date:{} ,status:{}".format(
            self.name,self.phone_number,self.email,self.service,self.start_date,self.end_date,self.status)
