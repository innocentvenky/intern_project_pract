from django.db import models
import uuid

# Create your models here.
class Register(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length= 20)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
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