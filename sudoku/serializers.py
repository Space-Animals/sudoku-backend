from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.user import User
from .models.game import Game

class GameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Game
    fields= '__all__'
    # fields = ('id', 'cells', 'over', 'time', 'owner', 'created_at', 'updated_at')

class UserSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'games')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)
