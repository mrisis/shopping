from rest_framework import serializers
from accounts.models import User



class UserListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=100)
    full_name = serializers.CharField(max_length=100)
    is_active = serializers.BooleanField(default=True)
    is_admin = serializers.BooleanField(default=False)


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    full_name = serializers.CharField(max_length=100,required=True)
    phone_number = serializers.CharField(max_length=11,required=True)
    password = serializers.CharField(max_length=50,write_only=True,required=True)

    def validate_email (self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_phon_number(self,value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Phone Number already exists")




