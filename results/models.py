from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=20, unique=True)
    batch = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name},{self.roll_number}"
    
class Subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    max_marks = models.IntegerField(default=100)

    def __str__(self):
        return self.name
    
class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='Result')
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    exam_date = models.DateField(auto_now_add=True)


    class Meta:
        unique_together = ('student','subject')

    def __str__(self):
        return f"{self.student} : {self.subject}"
    