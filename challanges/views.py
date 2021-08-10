from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Challanges
from rest_framework.permissions import IsAuthenticated


class TeacherChallangesView(generics.ListCreateAPIView):
    queryset = Challanges.objects.all()
    ordering = ['-created']
    serializer_class = ChallagesSerializer


class StudentChallangesView(generics.ListCreateAPIView):
    ordering = ['-created']
    serializer_class = ChallagesSerializer

    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Challanges.objects.all()[:3]
        #return Challanges.objects.filter(challanges_students__customuser_id=self.kwargs['student_class_id'])
        #return Challanges.objects.filter(students__pk=self.request.user.pk)
        #return CustomUser.objects.filter(role="Student", studentprofile__student_class=self.kwargs['student_class_id'])

class StudentRecommenderChallangesView(generics.ListCreateAPIView):
    ordering = ['-created']
    serializer_class = ChallagesSerializer

    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Challanges.objects.all()[:3]


#############for debug#############################################################################
class ChallangeView(generics.ListCreateAPIView):
    # ordering = ['-created']
    serializer_class = ChallagesSerializer

    def get_queryset(self):
        return Challanges.objects.filter(challanges_id=self.kwargs['challange_id'])


#   Report Api code...

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


@api_view(['GET', 'POST'])
def get_report(request):
    if request.method == 'GET':
        return Response({"Msg": "Send POST Request for Report"})

    if request.method == 'POST':
        std_id = request.data.get('student_id', None)
        if std_id != None:
            challenge_id = request.data.get('challenge_id', None)
            if challenge_id != None:
                try:
                    std = CustomUser.objects.get(id=std_id)
                except CustomUser.DoesNotExist:
                    return Response({"Msg": "No Student Against this id"})
                try:
                    chalenge = Challanges.objects.get(id=challenge_id)
                except Challanges.DoesNotExist:
                    return Response({"Msg": "No Challenge Against this id"})

                compl_challenge = Completed_Challange(challenge=chalenge, student=std)
                compl_challenge.save()
                res = {
                    "Msg": "Challenge added updated"
                }
                return Response(res)
            try:
                std = CustomUser.objects.get(id=std_id)
                try:
                    Total_Std_Challenges = Challanges.objects.filter(students=std).count()
                    completed = Completed_Challange.objects.filter(student=std).count()
                    if Total_Std_Challenges > completed:
                        un_completed = Total_Std_Challenges - completed
                    else:
                        un_completed = completed - Total_Std_Challenges
                    response = {
                        "Total_Challenges": Total_Std_Challenges,
                        "un_completed": un_completed,
                        "completed": completed,
                        "last_login": std.last_login,
                    }
                    # chellenges = Completed_Challange.objects.filter(student=std)
                    # ser = Completed_ChallangeSerializer(chellenges,many=True)
                    return Response(response)
                except Completed_Challange.DoesNotExist:
                    return Response({"Msg": "No Challenges found Against this id"})
            except CustomUser.DoesNotExist:
                return Response({"Msg": "No Student Against this id"})
        else:
            return Response({"Msg": "Send POST Request for Report"}) \
 \
 \
@api_view(['GET', 'POST'])
def forget_password(request):
    if request.method == 'GET':
        all_forget = Forget_password.objects.all().order_by('-id')
        ser = Forget_passwordSerializer(all_forget, many=True)
        return Response(ser.data)

    if request.method == 'POST':
        std_id = request.data.get('student_id', None)
        if std_id != None:
            try:
                std = CustomUser.objects.get(id=std_id)
                forget = Forget_password(student=std)
                forget.save()

                return Response({'msg': "Request sent to teacher"})
            except CustomUser.DoesNotExist:
                return Response({"Msg": "No Student Against this id"})


@api_view(['GET', 'POST'])
def issue_challenge(request):
    if request.method == 'GET':
        issued_challenges = Issue_Challange.objects.all().order_by('-id')
        ser = Issue_ChallangeSerializer(issued_challenges, many=True)
        return Response(ser.data)

    if request.method == 'POST':
        std_id = request.data.get('student_id', None)
        if std_id != None:
            challenge_id = request.data.get('challenge_id', None)
            if challenge_id != None:
                try:
                    std = CustomUser.objects.get(id=std_id)
                except CustomUser.DoesNotExist:
                    return Response({"Msg": "No Student Against this id"})
                try:
                    chalenge = Challanges.objects.get(id=challenge_id)
                except Challanges.DoesNotExist:
                    return Response({"Msg": "No Challenge Against this id"})

                issue_challenge = Issue_Challange(challenge=chalenge, student=std)
                issue_challenge.save()
                res = {
                    "Msg": "Challenge isued"
                }
                return Response(res)
        else:
            return Response({"Msg": "Send POST Request for Report"})
