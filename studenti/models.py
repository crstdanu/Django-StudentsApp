from django.db import models

# Create your models here.


class Student(models.Model):
    numar_matricol = models.PositiveIntegerField()
    prenume = models.CharField(max_length=50)
    nume = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    specializarea = models.CharField(max_length=50)
    media = models.FloatField()

    def __str__(self):
        return f'Student: {self.prenume} {self.nume}'
