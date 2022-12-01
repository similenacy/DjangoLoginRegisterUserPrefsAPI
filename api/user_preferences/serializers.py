from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User_Preference


class UserPrefSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = User_Preference
        fields =['color', 'music', 'food', 'drink', 'user']
