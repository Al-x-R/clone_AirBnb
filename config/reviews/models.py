from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):
    review = models.TextField()
    accuracy = models.FloatField()
    communication = models.FloatField()
    check_in = models.FloatField()
    location = models.FloatField()
    cleanliness = models.FloatField()
    value = models.FloatField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review} - {self.room}'

    def rating_average(self):
        avg = (
                      self.accuracy
                      + self.communication
                      + self.cleanliness
                      + self.location
                      + self.check_in
                      + self.value
              ) / 6
        return round(avg, 2)

    rating_average.short_description = "Avg."

    class Meta:
        ordering = ("-created",)

