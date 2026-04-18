from django.db import models

class Student(models.Model):
    student_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=200)
    credit_points = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.code} - {self.title}"


class Enrolment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student} - {self.course} - {self.semester} {self.year}"