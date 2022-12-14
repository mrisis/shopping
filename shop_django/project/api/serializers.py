from rest_framework import serializers



class UserListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=100)
    full_name = serializers.CharField(max_length=100)
    is_active = serializers.BooleanField(default=True)
    is_admin = serializers.BooleanField(default=False)

