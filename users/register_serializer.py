from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100, min_length=3, allow_blank=False)
    last_name = serializers.CharField(max_length=100, min_length=3, allow_blank=False)
    email = serializers.EmailField(allow_blank=False)
    password = serializers.CharField(min_length=6, style={'input_type': 'password'}, read_only=True, allow_blank=False)
    confirm_password = serializers.CharField(min_length=6, style={'input_type': 'password'}, read_only=True, allow_blank=False)
    

