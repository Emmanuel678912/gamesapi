from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Game
from .serializers import GameSerializer, UserRegistrationSerializer
from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ViewSet 


# Create your views here.
class GameView(viewsets.ModelViewSet):
    # obtain Game data from database and display it on the page 
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class NewGameView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def create(self, request):
        name = request.POST.get('name')
        genre = request.POST.get('genre')
        price = request.POST.get('price')
        file = request.POST.get('files')


        game, created = Game.objects.get_or_create(
            name = name,
            genre = genre,
            price = price,
            files = file,
        )

        game.save()
    
        return redirect('/')
        


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    # allow user to register and if it fails then send them back to the login page
    def post(self, request, *args, **kwargs):
        try:
            serializer = UserRegistrationSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                token = Token.objects.get(user=user).key
                data = {'token' : token}
            else:
                data = serializer.errors
                return Response(data=data, status=201)
        
        except Exception:
            return redirect('/login')

        

class LoginView(generics.CreateAPIView):
    serializer_class = AuthTokenSerializer

    # create an authentication token and use it as a view
    def create(self, request):
        return ObtainAuthToken().as_view()(request=request._request)
