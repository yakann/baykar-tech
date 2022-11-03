from django.db import models
from django.contrib.auth.models import AbstractUser
from enumfields import EnumField
from users.enums import UserType
from utils.models import StarterModel


class BaykarCustomer(StarterModel, AbstractUser):
    email_allowed = models.BooleanField(default=False)
    sms_allowed = models.BooleanField(default=False)
    user_type = EnumField(UserType, null=True, blank=True)
