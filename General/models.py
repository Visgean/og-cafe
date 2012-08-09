from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length = 20)
    teacher = models.ForeignKey(User, related_name = "subject_teacher")
    students = models.ManyToManyField(User, related_name = "subject_students")

    def __unicode__(self):
        return self.name
    
    class Meta:
        permissions = (
               ("list_subject", "can list whole class/subject"),
                        )

class Semester(models.Model):
    semester = models.IntegerField()
    name = models.CharField(max_length = 20, null = True, blank = True)
    
    def __unicode__(self):
        return str(self.semester)

