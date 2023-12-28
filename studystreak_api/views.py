from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect, JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
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

from studystreak_api.utils import get_user_role

from .form import RedirectForm
from .renderers import UserRenderes
from .serializers import (
    ChangePasswordSerializer,
    LoginSerializer,
    PasswordResetSerializer,
    RedirectLinkSerializer,
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


from django.contrib.sites.shortcuts import get_current_site

from students.models import Student
from studystreak_api.utils import account_activation_token


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
            current_site = get_current_site(request)
            token = account_activation_token.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            # link = f"{current_site.domain}/confirm/{uid}/{token}"
            context = {
                "domain": current_site.domain,
                "uid": uid,
                "token": token,
            }
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
    authentication_classes = []
    permission_classes = []

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
                user_role = get_user_role(user)

                return Response(
                    {
                        "token": token,
                        "msg": "Login Successful",
                        "userid": user.id,
                        "user_status": user_group,
                        "user_role": user_role,
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
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    renderer_classes = [UserRenderes]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )
        print(serializer)
        print("****")
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


class RedirectLinkView(APIView):
    renderer_classes = [UserRenderes]

    def post(self, request, uid, token, format=None):
        serializer = RedirectLinkSerializer(
            data=request.data, context={"uid": uid, "token": token}
        )

        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "password reset successfully"}, status=status.HTTP_200_OK
            )


from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.http import HttpResponse
from django.utils.encoding import force_bytes, smart_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


def userresetpassword(request, uid, token):
    try:
        id = smart_str(urlsafe_base64_decode(uid))
        user = User.objects.get(id=id)
    except Exception:
        return HttpResponse("user not found")
        # return "user not found"
        print("")

    if PasswordResetTokenGenerator().check_token(user, token):
        form = RedirectForm
        if form.is_valid():
            form.save()
            # return render(request, "successful.html")
            return HttpResponse("successgull")
            # templates success=mess
        else:
            return HttpResponse("form is not valid")
            # return render({"form":"password and password2 not match"})
        # if password == password2:
        #         user.set_password(password)
    #     user.save()
    #     return render("msg resetsuccessfull")
    # else:
    #     return render("msg resetunsuccessfull")
    # render a form with pass1 and pass2
    # form = RedirectForm
    # user = User.objects.get(id=id)

    # try:

    # except DjangoUnicodeDecodeError as indentifier:
    #     PasswordResetTokenGenerator().check_token(user,token)
    #     raise serializers.ValidationError("Token is not valid or expired.")


import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from studystreak_api.utils import account_activation_token


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


def confirm_user(request, uid, token):
    try:
        user_id = force_bytes(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=user_id)

    except Exception:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        link = f"http://{get_current_site(request).domain}"
        user.save(update_fields=["is_active"])

        return render(request, "emails/account-active.html", context={"link": link})
        return HttpResponseRedirect(f"http://{get_current_site(request).domain}")

    else:
        return HttpResponse("Some error occured.")


class GetUserRole(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response(get_user_role(request.user), 200)
