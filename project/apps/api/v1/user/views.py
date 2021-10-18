from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class Login(APIView):
    def post(self, request, *args, **kwargs):
        return Response(status = status.HTTP_200_OK)

class Register(APIView):
    def post(self, request, *args, **kwargs):
        return Response(status = status.HTTP_200_OK) 

class Logout(APIView):
    permission_classes = (IsAuthenticated)

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status = status.HTTP_200_OK)

class User(APIView):
    permission_classes = (IsAuthenticated)

    def get(self, request, *args, **kwargs):
        content = {'message': 'Hello, World!'}
        return Response(content)