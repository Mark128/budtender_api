from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    strain = models.CharField(max_length=50)
    event_info = models.JSONField(null=True, blank=True)
    event_datetime = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.strain} at {str(self.event_datetime)}"
