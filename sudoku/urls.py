from django.urls import path
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.game_views import Games, GamesDetail

urlpatterns = [
	# Restful routing; contains each of the app's separate routes
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('games/', Games.as_view(), name='games'),
    path('games/<int:pk>/', GamesDetail.as_view(), name='games-detail'),
]
