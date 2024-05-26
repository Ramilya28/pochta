from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def change_position(self, new_position):
        self.position = new_position
        self.save()