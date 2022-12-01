
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

    def get(self, request, format=None):
        queryset = User_Preference.objects.all()
        serializer = UserPrefSerializer(queryset, many=True)
        return Response(serializer.data)


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

    
