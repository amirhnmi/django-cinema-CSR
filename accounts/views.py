from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer,ForgetPasswordSerializer,PasswordResetSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
# Create your views here.

class RegisterApiView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LoginApiView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request=request,email=email, password=password)
        if user is not None:
            login(request, user=user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class UserDetailView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        token_key = request.data.get('token')

        token_obj = Token.objects.get(key=token_key)
        user = token_obj.user

        user_data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            "phone_number":user.phone_number
        }

        return Response(user_data, status=status.HTTP_200_OK)


# password reset --------------

class ForgetPasswordView(APIView):
    def post(self, request):
        serializer = ForgetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response({'error': 'User not found.'}, status=status.HTTP_400_BAD_REQUEST)
            # Generate a unique token for the password reset link
            token, _ = Token.objects.get_or_create(user=user)
            user.auth_token = token
            user.save()
            # Send an email to the user with a password reset link
            subject = 'Password Reset For CinemaTicket'
            message = f'Please click the following link to reset your password: http://localhost:3000/auth/login/password_reset/{token}'
            from_email = "mr.arhnmi@gmail.com"
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return Response({'success': 'Password reset email has been sent.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            token = request.data.get('token')
            password = request.data.get("password")

            try:
                user = CustomUser.objects.get(auth_token=token)
            except CustomUser.DoesNotExist:
                return Response({'error': 'Invalid token1.'}, status=status.HTTP_400_BAD_REQUEST)

            
            token_generator = PasswordResetTokenGenerator()
            if token_generator.check_token(user, token):
                user.set_password(password)
                user.save()
                
                return Response({'success': 'Password has been reset.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid token.', 'user_email': user.email, "auth_token":token,"password":password}, status=status.HTTP_400_BAD_REQUEST)
                # return Response({'error': 'Invalid token11.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

