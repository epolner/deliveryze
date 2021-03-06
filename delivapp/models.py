from django.db import models
from django.contrib.auth.models import User

class DeliveryzeUser(models.Model):
  user = models.OneToOneField(User)

  isDriver = models.BooleanField()
  address = models.CharField(max_length=100)
  zipCode = models.CharField(max_length=10)
  phoneNumber = models.CharField(max_length=15)

  def __unicode__(self):
    return self.user.username
