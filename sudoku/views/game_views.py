from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
# from django.contrib.auth import get_user, authenticate, login, logout

from ..serializers import GameSerializer
# from ..models.user import User

# Routing-ish Stuff
class Games(APIView):
  # Get Request
  def get(self, request):
    """Index Request"""
    print(request)
    games = Game.object.all()
    data = GameSerializer(games, many=True).data
    return Response(data)

  # Post Request
  def post(self, request):
    """Post Request"""
    print(request.data)
    game = GameSerializer(data=request.data['game'])
    if game.is_valid():
      g = game.save()
      return Response(game.data, status=status.HTTP_201_CREATED)
    else:
      return Response(game.errors, status=status.HTTP_400_BAD_REQUEST)
