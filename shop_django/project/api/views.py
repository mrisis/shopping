from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import User
from .serializers import UserListSerializer


class UserListAPIView(APIView):
    def get(self,request):
        users = User.objects.filter(is_active=True)
        ser_data = UserListSerializer(instance=users , many=True)
        return Response(data = ser_data.data)
