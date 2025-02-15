from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .serializers import UserRegistrationSerializer
from .models import User
from django.middleware.csrf import get_token
from django.http import JsonResponse

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully. Check email for OTP."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationVerifyView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        user = User.objects.filter(email=email, otp=otp).first()
        if user:
            user.is_verified = True
            user.save()
            return Response({"message": "User verified successfully."}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            response = Response({"message": "Login successful."}, status=status.HTTP_200_OK)
            response.set_cookie('auth_token', user.auth_token.key, httponly=True, secure=True)
            return response
        return Response({"message": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'email': user.email,
            'is_verified': user.is_verified,
        })

class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        response = Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
        response.delete_cookie('auth_token')
        return response
    
class CSRFTokenView(APIView):
    def get(self, request):
        token = get_token(request)
        return JsonResponse({'csrfToken': token})