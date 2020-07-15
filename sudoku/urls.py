from django.urls import path
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.game_views import GameIndex, GameCreate

urlpatterns = [
	# Restful routing
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),

    path('games/', GameIndex.as_view(), name='games'),
    path('games/', GameCreate.as_view(), name='games')
]
