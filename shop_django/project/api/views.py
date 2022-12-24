from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import User
from .serializers import UserListSerializer , UserRegisterSerializer


class UserListAPIView(APIView):
    def get(self,request):
        users = User.objects.filter(is_active=True)
        ser_data = UserListSerializer(instance=users , many=True)
        return Response(data = ser_data.data)


class UserRegisterApiView(APIView):
    def post(self,request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            User.objects.create_user(phone_number=ser_data.validated_data['phone_number']  ,
                                     email=ser_data.validated_data['email'] ,
                                     full_name=ser_data.validated_data['full_name'] ,
                                     password=ser_data.validated_data['password']
                                     )
            return Response(ser_data.data)
        return Response(ser_data.errors)

