from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Charging_Station_table(models.Model):
    LOGIN=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    contact=models.BigIntegerField()
    status=models.CharField(max_length=100)
    latitude=models.FloatField()
    longitude=models.FloatField()




class Worker_table(models.Model):
    CHARGE_STATION=models.ForeignKey(Charging_Station_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.IntegerField()
    status=models.CharField(max_length=100)


class Feedback_table(models.Model):
    LOGIN = models.ForeignKey(User,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=100)
    date=models.DateField()




class User_table(models.Model):
    LOGIN = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.IntegerField()


class Complaint_table(models.Model):
    USER=models.ForeignKey(User_table,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    date=models.DateField()
    Reply=models.CharField(max_length=100)


class Charging_slot_table(models.Model):
    CHARGING_STATION=models.ForeignKey(Charging_Station_table,on_delete=models.CASCADE)
    slot_number=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    start_time=models.TimeField()
    end_time=models.TimeField()
    amount=models.CharField(max_length=100,default='200')


class public_station_table(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    type = models.CharField(max_length=100)


class Charging_station_feedback_table(models.Model):
    USER=models.ForeignKey(User_table,on_delete=models.CASCADE)
    CHARGING_STATION=models.ForeignKey(Charging_Station_table,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=100)
    date=models.DateField()


class Charging_slot_booking_table(models.Model):
    USER=models.ForeignKey(User_table,on_delete=models.CASCADE)
    SLOT=models.ForeignKey(Charging_slot_table,on_delete=models.CASCADE)
    booking_date=models.DateField()
    status=models.CharField(max_length=100)

class Chat_table(models.Model):
    from_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name="k")
    To_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name="ll")
    message=models.CharField(max_length=100)
    date=models.DateField()

class Payment(models.Model):
    BOOKING=models.ForeignKey(Charging_slot_booking_table,on_delete=models.CASCADE)
    amount=models.IntegerField()
    status=models.CharField(max_length=100)
    date=models.DateField()


class Service_request(models.Model):
    USER=models.ForeignKey(User_table,on_delete=models.CASCADE)
    CHARGING_STATION=models.ForeignKey(Charging_Station_table,on_delete=models.CASCADE)
    service=models.CharField(max_length=100)
    date=models.DateField()
    status=models.CharField(max_length=100)

class Assign_service_table(models.Model):
    WORKER=models.ForeignKey(Worker_table,on_delete=models.CASCADE)
    REQUEST=models.ForeignKey(Service_request,on_delete=models.CASCADE)
    date=models.DateField()



class Category_table(models.Model):
    category_type=models.CharField(max_length=100)
    date=models.DateField()



class Charging_station_category_table(models.Model):
    CATEGORY=models.ForeignKey(Category_table,on_delete=models.CASCADE)
    CHARGING_STATION=models.ForeignKey(Charging_Station_table,on_delete=models.CASCADE)
    date=models.DateField()






