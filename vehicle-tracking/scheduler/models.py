from django.db import models

class Vehicle(models.Model):
    VIN = models.AutoField(unique=True,primary_key=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    latitude = models.FloatField()  # Use FloatField for latitude/longitude
    longitude = models.FloatField()
    driver = models.ForeignKey('user.Driver', on_delete=models.SET_NULL, null=True, related_name='vehicles')



    class Meta:
        db_table = "vehicles"


class Driver(models.Model):
    license_number = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    class Meta:
        db_table = "drivers"


class Route(models.Model):
    start_latitude = models.FloatField()
    start_longitude = models.FloatField()
    end_latitude = models.FloatField()
    end_longitude = models.FloatField()
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, related_name='routes')
    
    def __str__(self):
        return f"Route from ({self.start_latitude}, {self.start_longitude}) to ({self.end_latitude}, {self.end_longitude})"

    class Meta:
        db_table = "routes"


class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return f"Location of vehicle {self.vehicle.VIN}"

    class Meta:
        db_table = "locations"


class Schedule(models.Model):
    route_id = models.ForeignKey('Route', on_delete=models.CASCADE, related_name='schedules')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Schedule for Route ID {self.route_id}"

    class Meta:
        db_table = "schedulers"
