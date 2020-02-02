from django.db import models

from pontos_turisticos.address.models import Address
from pontos_turisticos.attractions.models import Attraction
from pontos_turisticos.comments.models import Comment
from pontos_turisticos.evaluations.models import Evaluation


class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    evaluations = models.ManyToManyField(Evaluation)
    address = models.ForeignKey(Address, on_delete=models.CASCADE,
                                null=True, blank=True)

    def __str__(self):
        return self.name
