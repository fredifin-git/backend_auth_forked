from django.http import HttpResponse

from .serializers import *

from challanges.models import *
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import json

@api_view(['GET','POST'])
def student_notif(request):

    if request.method == 'GET':
       return Response({"msg":"Send POST Request with stdudent_id  for Challenge notifi "})


    if request.method == 'POST':
        std_id = request.data.get('student_id', None)
        challenge_id = request.data.get('challenge_id', None)
        if std_id != None:
            try:
                std = CustomUser.objects.get(id=std_id)
            except CustomUser.DoesNotExist:
                return Response({"Msg": "No student Against this id"})
            if challenge_id != None:
                # teacher will send std id and challenge id that due date is 3 days!
                try:
                    chalenge = Challanges.objects.get(id=challenge_id)
                except Challanges.DoesNotExist:
                    return Response({"Msg": "No Challenge Against this id"})
                msg = "You have pending challenge "+ str(chalenge.Title) + " due date is" + str(chalenge.last_date)
                Due_chlnge = DueChallenge(student=std, msg=msg)
                Due_chlnge.save()
                all_due_chlnge = DueChallenge.objects.filter(student=std).order_by('-id')
                ser = DueChallengeSerializer(all_due_chlnge, many=True)
                return Response(ser.data)
                    # notification when on all challenges... on each student.
            try:
                        Total_Std_Challenges = Challanges.objects.filter(students=std).order_by('-id')
                        ser = ChallageNotifSerializer(Total_Std_Challenges, many=True)
                        return Response(ser.data)
            except Challanges.DoesNotExist:
                        return Response({"Msg": "No Challenges found Against this id"})
        else:
            return Response({"Msg":"None is not acceptable"})



from django.db.models import Q
@api_view(['GET'])
def teacher_notif(request):
    if request.method == 'GET':

                    #  Last Date Should be larger and ans of dates is 3 then show msg...
                    challenges = Challanges.objects.filter(
                                                                Q(last_date__gte=datetime.datetime.now().date())
                                                                |
                                                                Q(last_date=datetime.datetime.now().date())
                                                                )
                    Final_list = []
                    for ch in challenges:
                        date = ch.last_date - datetime.datetime.now().date()
                        days = date.days
                        if days<=3:
                            msg="You have a due chalange "+ch.Title+" Due date "+str(ch.last_date)
                            x={
                                "msg":str(msg)
                              }
                            Final_list.append(x)
                    json_data = JSONRenderer().render(Final_list)
                    return HttpResponse(json_data, content_type="application/json")


    else:
            return Response({"Msg":"None is not acceptable"})


