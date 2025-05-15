from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Artisan, Customer, User

User = get_user_model()


@api_view(['POST'])
def register_user(request):
    data = request.data

    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email já está em uso.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(
        email=email,
        username=username,
        password=make_password(password)
    )

    return Response({'message': 'Usuário criado com sucesso.'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_user(request):
    data = request.data

    email = data.get('email')
    password = data.get('password')

    user = authenticate(request, email=email, password=password)

    if user:
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)