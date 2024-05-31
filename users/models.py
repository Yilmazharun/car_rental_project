from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager
from django.core.validators import RegexValidator


class User(BaseUser):
    phone_regex = RegexValidator(
        regex=r"^\(\d{3}\) \d{3}-\d{4}$",
        message="Phone number must be entered in the format: (999) 999-9999"
    )
    
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    phoneNumber = models.CharField(validators=[phone_regex], max_length=17)
    address = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=7)
    builtIn = models.BooleanField(default=False)
    roles = models.CharField(max_length=255)
    confirmPassword = models.CharField(max_length=30)

    
    objects = BaseUserManager()
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"