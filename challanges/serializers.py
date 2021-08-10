from rest_framework import serializers
from .models import *


class ChallagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challanges
        fields = ('id', 'Title', 'Social', 'Emotional', 'Study', 'Personal', 'completed', 'students')


class StudentChallangesSerializer(serializers.ModelSerializer):
    class Meta:
        models = Challanges
        fields = '__all__'

class Completed_ChallangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Completed_Challange
        fields = '__all__'


class Issue_ChallangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue_Challange
        fields = '__all__'

class Forget_passwordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forget_password
        fields = '__all__'
