from django.contrib.auth.models import User, Permission, Group

"""
This module contains methods which should be called after some key groups were created

"""


def configureTeachers():
    permissionList = ["list_subject"]
    teachers, created = Group.objects.get_or_create(name = "teachers")
    
    perms = Permission.objects.filter(codename__in = permissionList)
    teachers.permissions.add(*perms)

def configureStudents():
    "so far there are no things that should be done for students"
    students, created = Group.objects.get_or_create(name = "students")


if __name__ == "__main__":
    configureStudents()
    configureTeachers()



