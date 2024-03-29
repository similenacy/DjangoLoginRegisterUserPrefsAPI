from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User_Preference


class UserPrefSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(source='user.id', read_only=True)
    user_name = serializers.PrimaryKeyRelatedField(source='user.username', read_only=True)

    class Meta:
        model = User_Preference
        fields =['color', 'music', 'food', 'drink', 'user','user_name']




