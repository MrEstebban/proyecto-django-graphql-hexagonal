from django.db import models

class Grade(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # Usando id como primary key
    student_id = models.CharField(max_length=50)           # Id del estudiante
    subject = models.CharField(max_length=100)             # Materia
    grade = models.FloatField()                            # Nota

    def __str__(self):
        return f"{self.student_id} - {self.subject} - {self.grade}"

class Student(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"