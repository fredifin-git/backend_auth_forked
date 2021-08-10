from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentClassSerializer, StudentClassStudentSerializer
from .models import StudentClass
from users.models import CustomUser


class StudentClassView(generics.ListCreateAPIView):
    queryset = StudentClass.objects.all()
    ordering = ['-created']
    serializer_class = StudentClassSerializer


class StudentClassStudentsView(generics.ListCreateAPIView):
    ordering = ['-created']
    serializer_class = StudentClassStudentSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(role="Student", studentprofile__student_class=self.kwargs['student_class_id'])
