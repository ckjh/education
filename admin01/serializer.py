from rest_framework import serializers
from admin01.models import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserLevelserializer(serializers.ModelSerializer):
    class Meta:
        model = UserLevel
        fields = "__all__"

