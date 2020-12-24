from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
User = get_user_model()

# Create your views here.


class SignInView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        email = data['email']
        password = data['password']

        try:
            user = User.objects.get(email=email)
            serializer = UserSerializer(user)
            return Response(serializer.data)

        except:
            return Response(False)


class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        email = data['email']
        password = data['password']

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists', 'status': 400})

        if(len(password) < 6):
            return Response({'error': 'Passwords is less than 6 characters', 'status': 411})

        user = User.objects.create_user(email=email, password=password)
        user.save()
        serializer = UserSerializer(user)
        return Response({'user': serializer.data, 'status': 201})


class GetUserView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, *args, **kwargs):
        id = kwargs['id']

        try:
            user = User.objects.get(id=id)
        except:
            return Response("User does not exist")

        serializer = UserSerializer(user)

        return Response(serializer.data)


class ProfileView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        id = data['id']
        name = data['userName']
        phone = data['phone']
        address = data['address']

        user = User.objects.get(id=id)
        user.name = name
        user.phone = phone
        user.address = address
        user.save()

        return Response('success')
