from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.models import StarterModel
# Create your models here.


class BaykarCustomer(AbstractUser, StarterModel):
    email_allowed = models.BooleanField(default=False)
    sms_allowed = models.BooleanField(default=False)

