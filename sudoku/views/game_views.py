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

class Games(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  def get(self, request):
    """Index Request"""
    games = Game.objects.filter(owner=request.user.id)
    data = GameSerializer(games, many=True).data
    return Response(data)

  serializer_class = GameSerializer
  def post(self, request):
    """Create Request"""
    request.data['owner'] = request.user.pk
    request.data['cells'] = [""]*81
    game = GameSerializer(data=request.data)
    if game.is_valid():
      game.save()
      return Response(game.data, status=status.HTTP_201_CREATED)
    else:
      return Response(game.errors, status=status.HTTP_400_BAD_REQUEST)
