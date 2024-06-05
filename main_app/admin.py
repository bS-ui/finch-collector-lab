from django.contrib import admin
# import your models here
from .models import Car, Service

# Register your models here
admin.site.register(Car)
admin.site.register(Service)