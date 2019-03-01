from django.conf import settings
from django.db import models, transaction

from django.contrib.auth import get_user_model
User = get_user_model()

class Bike(models.Model):
    image = models.ImageField(blank=True, null=False, upload_to = 'images/bikes/')
    number = models.CharField(max_length=10, null=False, default="https://")
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    helmet = models.BooleanField(default=True)
    gf_lat = models.DecimalField(max_digits=16, decimal_places=10)
    gf_lon =  models.DecimalField(max_digits=16, decimal_places=10)
    gf = models.BooleanField(default=True)
    gf_limit = models.IntegerField(default=10)
    speed = models.BooleanField(default=True)
    speed_limit = models.IntegerField(default=60)
    token = models.CharField(max_length=40)

    def __str__(self):
        return str(self.number)

class BikeStatus(models.Model):
    STATUS_CHOICES = (
        ("ON", "ON"),
        ("OFF", "OFF"),
        ("EMERGENCY", "EMERGENCY"),
        ("LOST", "LOST"),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    current_lat = models.DecimalField(max_digits=16, decimal_places=10)
    current_lon = models.DecimalField(max_digits=16, decimal_places=10)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=False)
    def __str__(self):
        return str(self.bike) + "-" + str(self.status)


class RideSummary(models.Model):
    ride_coordinates = models.TextField()
    driver = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='summaries')
    avg_speed = models.IntegerField(default=0)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now_add=True)
    helmet = models.BooleanField(default=True)
    def __str__(self):
        return str(self.bike) + "-" + str(self.start_time)

class BikeAccess(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='access')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('bike', 'user',)

    def __str__(self):
        return str(self.bike) + "-" + str(self.user)

class BikeAccessRequest(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='requests')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('bike', 'user',)
        
    def __str__(self):
        return str(self.bike) + "-" + str(self.user)