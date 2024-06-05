from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Mod(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('mod-detail', kwargs={'pk': self.id})
class Car(models.Model):
  model = models.CharField(max_length=100)
  year = models.IntegerField()
  description = models.TextField(max_length=250)
  mods = models.ManyToManyField(Mod)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.model
  
  def get_absolute_url(self):
    return reverse('car-detail', kwargs={'car_id': self.id})
  
class Service(models.Model):
  date = models.DateField('Service date')
  repair = models.CharField(max_length=250)

  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.repair} on {self.date}"
  
  class Meta:
    ordering = ['-date']
