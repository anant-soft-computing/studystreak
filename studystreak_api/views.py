from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView  # noqa: F811
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .renderers import UserRenderes
from .serializers import (
    ChangePasswordSerializer,
    LoginSerializer,
    PasswordResetSerializer,
    RegisterSerializer,
    ResetPasswordSerializer,
    UserProfileSerializer,
)


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({"li": csrf_token})


#################### Login #####################


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


from students.models import Student


class RegistrationView(APIView):
    # renderer_classes = [UserRenderes]
    # def post(self,request):
    #     serializer = RegisterSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         print(user)
    #         return Response({"msg": "Registration successful"}, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Student.objects.create(user=user)
            print(user)

            subject = "Registration Confirmation"
            message = "Thank you for registering!"
            recipient_list = [user.email]
            context = {}
            from_email = settings.EMAIL_HOST_USER
            html_message = render_to_string(
                "emails/email-verification.html", context=context
            )
            plain_message = strip_tags(html_message)

            message = EmailMultiAlternatives(
                subject=subject,
                body=plain_message,
                from_email=from_email,
                to=recipient_list,
            )

            message.attach_alternative(html_message, "text/html")
            message.send()
            return Response(
                {"msg": "Registration successful"}, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                try:
                    user_group = (Group.objects.get(user=user.id)).name
                except Exception:
                    user_group = "None"

                token = get_tokens_for_user(user)
                return Response(
                    {
                        "token": token,
                        "msg": "Login Successful",
                        "userid": user.id,
                        "user_status": user_group,
                    },
                    status=status.HTTP_200_OK,
                )

            return Response(
                {"errors": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(APIView):
    renderer_classes = [UserRenderes]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    renderer_classes = [UserRenderes]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )
        if serializer.is_valid(raise_exception=True):
            return Response({"msg": "Password changed"})

        return Response(serializer.errors)


class SendPasswordResetView(APIView):
    renderer_classes = [UserRenderes]

    def post(self, request, format=None):
        # try:
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "Password reset link is sent if it is registered"},
                status=status.HTTP_200_OK,
            )


class PasswordResetView(APIView):
    renderer_classes = [UserRenderes]

    def post(self, request, uid, token, format=None):
        serializer = ResetPasswordSerializer(
            data=request.data, context={"uid": uid, "token": token}
        )
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "password reset successfully"}, status=status.HTTP_200_OK
            )


import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView


@ensure_csrf_cookie
def set_csrf_token(request):
    """
    This will be `/api/set-csrf-cookie/` on `urls.py`
    """
    return JsonResponse({"details": "CSRF cookie set"})


def logout_view(request):
    """
    This will be `/api/logout/` on `urls.py`
    """
    logout(request)
    return JsonResponse({"detail": "Success"})


@require_POST
def login_view(request):
    """
    This will be `/api/login/` on `urls.py`
    """
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    if username is None or password is None:
        return JsonResponse(
            {"errors": {"__all__": "Please enter both username and password"}},
            status=400,
        )
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"detail": "Success"})
    return JsonResponse(
        {"detail": "Invalid credentials"},
        status=400,
    )


class CheckAuth(APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        if request.user and request.user.is_authenticated:
            return Response({"detail": "You're Authenticated"})

        else:
            return Response({"detail": "You're not Authenticated"})
