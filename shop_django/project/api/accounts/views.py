from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import User
from permissions import IsOwner
from .serializers import ProfileSerializer , ProfileEditSerializer


class ProfileApiView(APIView):


    '''
        method get:
            get user profile data
    '''

    permission_classes = [permissions.IsAuthenticated,IsOwner]

    def get(self,request,user_id):

        user =User.objects.get(id=user_id)
        self.check_object_permissions(request,user)
        ser_data = ProfileSerializer(instance=user)
        return Response(ser_data.data , status = status.HTTP_200_OK)


class ProfileEditApiView(APIView):
    '''
        method put:
          for edit and update user profile


    '''

    permission_classes = [permissions.IsAuthenticated,IsOwner]
    def put(self,request,user_id):
        user = User.objects.get(id=user_id)
        ser_data = ProfileEditSerializer(instance=user , data=request.data,partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data , status = status.HTTP_200_OK)
        return Response(ser_data.errors , status = status.HTTP_400_BAD_REQUEST)