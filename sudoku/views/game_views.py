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

# Game class; holds the CRUD methods to pass to the frontend for displaying on page
# With the converted data from Serializer, we can now return a response to the client
class Games(generics.ListCreateAPIView):
  # Trailing comma in the Tuple needed because python and tuples rules
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

class GamesDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  # pk refers to the game pk/id to grab the correct game. DELETE THIS AT END!
  def get(self, request, pk):
    """Show Request"""
    game = get_object_or_404(Game, pk=pk)
    data = GameSerializer(game).data
    if not request.user.id == data['owner']:
      raise PermissionDenied('Unauthorized. You don\'t own this game!')
    return Response(data)

  def delete(self, request, pk):
    """Delete Request"""
    game = get_object_or_404(Game, pk=pk)
    data = GameSerializer(game).data
    if request.user.id != data['owner']:
      raise PermissionDenied('Unauthorized. You don\'t own this game!')
    game.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)

  # if JSON, can block into | if object, can dot into
  # to save to DB has to be in object/model form, not JSON
  def partial_update(self, request, pk):
    """Update Request"""
    game = get_object_or_404(Game, pk=pk)
    if request.user.id != game.owner.id:
      raise PermissionDenied('Unauthorized. You don\'t own this game!')
    i = int(request.data['cell']['index'])
    game.cells[i] = request.data['cell']['value']
    request.data['owner'] = request.user.pk
    g = GameSerializer(game, data=request.data)
    if g.is_valid():
      g.save()
      return Response(g.data)
    else:
      return Response(g.errors, status = status.HTTP_400_BAD_REQUEST)
