
from django.http import Http404
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .models import User_Preference
from .serializers import UserPrefSerializer
from .permissions import OnlyOwnerCanView
from rest_framework.response import Response


# Create your views here

class UserPrefList(APIView):
    permission_classes = [OnlyOwnerCanView]

    def get(self, request, format=None):
        try:
            user = User_Preference.objects.get(pk=request.user.id)
            self.check_object_permissions(self.request, user)
            serializer = UserPrefSerializer(user)
            return Response(serializer.data)
        except User_Preference.DoesNotExist:
            return Http404


class UserPrefItem(APIView):
    permission_classes = [OnlyOwnerCanView]

    def get_object(self, pk):
        try:
            user = User_Preference.objects.get(pk=pk)
            self.check_object_permissions(self.request, user)
            return user
        except User_Preference.DoesNotExist:
            raise Http404

 
    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = UserPrefSerializer(instance)
        return Response(serializer.data)


class UserPrefItemByUser(APIView):
    permission_classes = [OnlyOwnerCanView]

    def get_object(self, userId):
        try:
            userPrefs = User_Preference.objects.get(pk = userId)
            self.check_object_permissions(self.request, userPrefs)
            return userPrefs
        except User_Preference.DoesNotExist:
            raise Http404

 
    def get(self, request, userId, format=None):
        instance = self.get_object(userId)
        serializer = UserPrefSerializer(instance)
        return Response(serializer.data)


    def patch(self, request, userId, format=None):
        instance = self.get_object(userId)
        serializer = UserPrefSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        raise Http404


class CheckSessionView(APIView):

    def get(self, request, format=None):
        hasSession = request.user.is_authenticated

        data = {
            'session' : hasSession
        }
        return Response(data)




    
