# В файле models.py
from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    professor = models.CharField(max_length=255)

    def __str__(self):
        return self.subject_name

class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.IntegerField()
    date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.subject.subject_name}"
