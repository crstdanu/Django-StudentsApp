import random
from django.test import TestCase
from .models import Student


# Create your tests here.

class StudentModelUnitTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            numar_matricol=random.randint(10000, 99999),
            prenume='Vasile',
            nume='Popescu',
            email='vasile@popescu.com',
            specializarea='Matematica',
            media=8.85
        )

    def test_student_model(self):
        data = self.student
        self.assertIsInstance(data, Student)
