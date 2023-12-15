from django.shortcuts import render
from rest_framework import generics
from .serializers import assessmentListSerializer
from .models import assessment
from rest_framework.generics import ListAPIView
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime as dt
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from rest_framework import (
    filters,
    generics,  # noqa: F811
    status,
)
from rest_framework.response import Response  # noqa: F811
from rest_framework.views import APIView  # noqa: F811
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import LoginSerializer
# Create your views here.

class assessmentListView(generics.ListCreateAPIView):
    queryset = assessment.objects.all()
    serializer_class = assessmentListSerializer
        
    
class assessmentRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = assessment.objects.all()
    serializer_class = assessmentListSerializer
    
    
#################### Login #####################

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


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

            return Response({"errors": {"msg": -1}}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
