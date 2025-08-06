from django.test import TestCase
from .models import Student, Course

class DRCTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name="Alice", age=22, department="CS")
        Course.objects.create(name="DBMS", student=self.student, grade="A")

    def test_drc_query(self):
        response = self.client.get('/drc-queries/')
        self.assertEqual(response.status_code, 200)
