from rest_framework import serializers

from apps.jack_app.models import Fruit, CreditUser

from django.contrib.auth.models import User


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = (
            'id',
            'name',
            'value',
            'img',
        )

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
        )
        
class CreditUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = CreditUser
        fields = (
            'id',
            'user',
            'credit',
        )
