from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100) 
    

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField('Student', related_name='teachers', blank=True)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    jwt_token_refresh = models.CharField(max_length=100, null=True, blank=True)
    jwt_token_access = models.CharField(max_length=100, null=True, blank=True)

    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Certificate for {self.student.name} from {self.teacher.name}"
