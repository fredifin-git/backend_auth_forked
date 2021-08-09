from rest_framework import serializers
from challanges.models import *
from .models import *

class ChallageNotifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challanges
        fields = ('id', 'Title')

class DueChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DueChallenge
        fields = '__all__'
