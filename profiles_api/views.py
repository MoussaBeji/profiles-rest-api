from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework import  viewsets
from rest_framework.authentication import  TokenAuthentication

from profiles_api import serializers
from profiles_api.models import UserProfile
from profiles_api import  permissions
class UserList(APIView):
    """Class to get list of users"""
    serializer_user = serializers.UserSerializer
    def get(self, request, format=None):
        """Return a list of APIView features"""

        users = UserProfile.objects.all()
        users_serializer = self.serializer_user(users, many=True)

        return Response({'Users_list': users_serializer.data})

    def post(self, request):
        """Return hello message with name"""
        user_serializer = self.serializer_user(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': "Added Successfully!!"})
        else:
            return Response(user_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """Class to manage the detais of a given user"""
    serializer_user = serializers.UserSerializer

    def put(self, request, pk=0):
        """Handel updating an object"""
        user_data = JSONParser().parse(request)
        user = UserProfile.objects.get(id=pk)
        user_serializer = self.serializer_user(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"message": "Updated Successfully"})
        else:
            return Response(user_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """Handel a partial update of an object"""
        user_data = JSONParser().parse(request)
        user = UserProfile.objects.get(id=pk)
        user_serializer = self.serializer_user(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"message": "Updated Successfully"})
        else:
            return Response(user_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=0):
        """Handel a partial update of an object"""
        user = UserProfile.objects.get(id=pk)
        user.delete()

        return Response({"message": "Deleted Succeffully!!"})


class UserViewset(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
