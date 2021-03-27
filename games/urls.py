from django.urls import path, include
from rest_framework import routers
from . import views

# access api from /games
router = routers.DefaultRouter()
router.register('games', views.GameView)

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.LoginView.as_view()),
    path('register', views.UserRegistrationView.as_view()),
]