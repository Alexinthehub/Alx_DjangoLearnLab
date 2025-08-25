# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # This line explicitly defines the password field.
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # This line uses the 'create_user' method.
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user