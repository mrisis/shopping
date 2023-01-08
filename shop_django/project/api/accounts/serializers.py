from rest_framework import serializers
from accounts.models import User



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','full_name','email','phone_number','image','is_active','is_admin','is_superuser')


class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name','email','phone_number')
