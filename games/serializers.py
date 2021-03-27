from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Game


# creates an API using JSON
class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'url', 'name', 'genre', 'price')

class UserRegistrationSerializer(serializers.ModelSerializer):
    # password
    password = serializers.CharField(style={'input type' : 'password'}, write_only=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    # create new user with data validation
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
