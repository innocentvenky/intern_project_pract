from django.db import models
import uuid
import re
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


# creating function for password validations
def strong_pass(value):
    if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$',value):
        raise ValidationError(
            "Password must contain one uppercase letter," \
            "Password must contain one lowercase letter," \
            "Password must contain one number," \
            "Password must contain one special character," \
            " Password must contain atleast 8 characters"
        )


# Create your models here.

class Register(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length= 20,validators=[strong_pass])
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=10,validators=[RegexValidator(regex=r'^\d{10}$',message='Phone number must contain  10 digitsonly')])
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    pincode = models.IntegerField()
    def __str__(self):
        return self.first_name