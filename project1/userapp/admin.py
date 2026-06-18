from django.contrib import admin
from userapp.models import Register
# Register your models here.
class Registeradmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','password','gender','date_of_birth','phone_number','city','state','pincode']
admin.site.register(Register,Registeradmin)