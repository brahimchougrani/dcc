from django.db import models

# Create your models here.

#students Model with speciality
class Speciality(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    student_id = models.PositiveIntegerField(unique=True)
    date_of_birth = models.DateField()
    speciality = models.ForeignKey(Speciality,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name
