from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=12)
    description = models.TextField()

    def __str__(self):
        return self.email
    
class Enrollment(models.Model):
    FullName = models.CharField(max_length=50)
    Email = models.EmailField()
    Gender = models.CharField(max_length=25)
    PhoneNumber = models.CharField(max_length=12)
    DOB = models.CharField(max_length=25)
    Address = models.CharField(max_length=250, blank=True, null=True)
    SelectMembershipPlan = models.CharField(max_length=50)
    SelectTrainer = models.CharField(max_length=50)
    Reference = models.CharField(max_length=50)
    PaymentStatus = models.CharField(max_length=50, blank=True, null=True)
    Price = models.IntegerField(blank=True, null=True)
    DueDate = models.DateTimeField(blank=True, null=True)
    TimeStamp = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.FullName

class Trainer(models.Model):
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=25)
    Phone = models.CharField(max_length=12)
    Salary = models.IntegerField()

    def __str__(self):
        return self.Name
    
class MembershipPlan(models.Model):
    Plan = models.CharField(max_length=50)
    Price = models.IntegerField()

    def __int__(self):
        return self.id
    
class Gallery(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __int__(self):
        return self.id

class Attendance(models.Model):
    Name=models.CharField(max_length=200)
    PhoneNumber=models.CharField(max_length=12)
    SelectDate=models.DateTimeField(auto_now_add=True)
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200)
    SelectWorkout=models.CharField(max_length=200)
    TrainedBy=models.CharField(max_length=200)

    def __int__(self):
        return self.id