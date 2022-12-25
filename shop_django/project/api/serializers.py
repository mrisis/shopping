from rest_framework import serializers
from accounts.models import User

class UserEditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','full_name','email','phone_number']


