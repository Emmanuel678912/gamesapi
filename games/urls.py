from django.urls import path, include
from rest_framework import routers
from . import views
#from .views import UploadViewSet

# access api from /games
router = routers.DefaultRouter()
router.register('games', views.GameView)

#router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.LoginView.as_view()),
    path('register', views.UserRegistrationView.as_view()),
    path('create', views.NewGameView.as_view()),
]