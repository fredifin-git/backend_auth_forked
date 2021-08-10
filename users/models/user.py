from django.contrib.auth.models import AbstractUser
from django.db import models
from classes.models import StudentClass
from django.contrib.postgres.fields import ArrayField


class CustomUser(AbstractUser):
    # Any extra fields would go here
    role = models.CharField(max_length=10, default='Student')
    phone = models.CharField(max_length=10, default='')
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    student_class = models.ForeignKey(StudentClass, on_delete=models.SET_NULL, null=True, related_name='students')
    sufficiencyLevel = models.IntegerField(default=0)
    # strongpoints = models.CharField(max_length=150, blank=True)
    # improvablepoints = models.CharField(max_length=150, blank=True)
    strongpoints =  ArrayField(
            models.IntegerField(default=0),
            size=28,
        )
    improvablepoints = ArrayField(
            models.IntegerField(default=0),
            size=26,
        )
    def __str__(self):
        return self.user.email


class TeacherProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    institutionID = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.email