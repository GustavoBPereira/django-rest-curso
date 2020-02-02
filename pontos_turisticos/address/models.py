from django.db import models


class Address(models.Model):
    line1 = models.CharField(max_length=155)
    line2 = models.CharField(max_length=155, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    lat = models.IntegerField(blank=True, null=True)
    long = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.line1
