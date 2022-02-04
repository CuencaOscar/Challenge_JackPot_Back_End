from apps.jack_app.models import CreditUser
from apps.jack_app.repositories import JackPotRepository
from apps.jack_app.serializers import FruitSerializer, CreditUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User

from apps.jack_app.services import JackPotService

# Create your views here.


class JackPotViewSet(viewsets.ViewSet):

    def list(self, request):
        data = JackPotRepository().getFruit()
        serializer = FruitSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def user(self, request):
        data = JackPotRepository().getCreditUSer()
        serializer = CreditUserSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def new_roll(self, request):
        data = request.data
        current_credits = int(data.get("current_credits"))
        user_id = int(data.get("user_id"))
        new_roll, new_credits = JackPotService().get_new_roll(current_credits)
        credit_user =  CreditUser.objects.get(user__id=user_id)
        credit_user.credit = current_credits + new_credits
        credit_user.save()
        res = {
            "new_roll": new_roll,
            "current_credits": current_credits,
            "new_credits": new_credits,
            "total_credits": current_credits + new_credits,
        }
        return Response(res, status=status.HTTP_200_OK)


class AuthenticationViewSet(viewsets.ViewSet):

    def sign_up(self, request):
        data = request.data
        email = data.get("email")
        user = User.objects.filter(email=email).all()
        if user:
            credit_user = CreditUser.objects.get(user=user[0])
            serializer = CreditUserSerializer(credit_user, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        user = User(
            email=email,
            password="aaaaaaa@aaa",
            username=email,
            first_name="",
            last_name="",
            is_staff=False,
            is_active=True,
            is_superuser=False,
        )
        user.save()
        credit_user = CreditUser(user=user, credit=10)
        credit_user.save()
        serializer = CreditUserSerializer(credit_user, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
