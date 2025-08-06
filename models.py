from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
