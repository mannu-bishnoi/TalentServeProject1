from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    linkedin=models.URLField(blank=True)
    twitter=models.URLField(blank=True)
    instagram=models.URLField(blank=True)
    facebook=models.URLField(blank=True)

    def __str__(self):
        return self.name

