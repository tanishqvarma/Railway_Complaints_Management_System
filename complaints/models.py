from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pnr = models.CharField(max_length=10)
    complaint = models.TextField()
    urgency = models.CharField(max_length=10)
    cleanliness = models.IntegerField()
    working = models.IntegerField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.pnr
