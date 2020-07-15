from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..serializers import GameSerializer, UserSerializer
from ..models.game import Game
# from ..models.user import User

# Routing-ish Stuff
# Get Request
class GameIndex(generics.ListCreateAPIView):
  serializer_class = GameSerializer
  permission_classes = (IsAuthenticated,)
  def get(self, request):
    """Index Request"""
    print(request.user)
    games = Game.objects.filter(owner=request.user.id)
    data = GameSerializer(games, many=True).data
    return Response(data)

# Post Request
class GameCreate(generics.ListCreateAPIView):
  serializer_class = GameSerializer
  permission_classes = (IsAuthenticated,)
  def post(self, request):
    """Post Request"""
    print(request.data)
    request.data['game']['owner'] = request.user.id
    game = GameSerializer(data=request.data['game'])
    if game.is_valid():
      g = game.save()
      return Response(game.data, status=status.HTTP_201_CREATED)
    else:
      return Response(game.errors, status=status.HTTP_400_BAD_REQUEST)
