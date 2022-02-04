from apps.jack_app.models import CreditUser
from apps.jack_app.serializers import CreditUserSerializer
import pytest
from django.contrib.auth.models import User


TEST_AUTH = [
    (
        'oscar@gmail.com',
        {
            "id": 1,
            "user": {
                "id": 1,
                "username": "oscar@gmail.com",
                "first_name": "",
                "last_name": "",
                "email": "oscar@gmail.com",
                "is_staff": False,
                "is_active": True
            },
            "credit": 10
        }
    ),
    (
        "qwerty@gmail.com",
        {
            "id": 2,
            "user": {
                "id": 2,
                "username": "qwerty@gmail.com",
                "first_name": "",
                "last_name": "",
                "email": "qwerty@gmail.com",
                "is_staff": False,
                "is_active": True
            },
            "credit": 10
        }
    )
]


@pytest.mark.parametrize(
    "email, expected",
    TEST_AUTH
)
@pytest.mark.django_db(transaction=True)
def test_create_user(email, expected):
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
    data = CreditUserSerializer(credit_user).data
    assert data.get('user').get('id') == expected.get('user').get('id')
    assert data.get('user').get('username') == expected.get('user').get('username')
    assert data.get('user').get('first_name') == expected.get('user').get('first_name')
    assert data.get('user').get('first_name') == expected.get('user').get('first_name')
    assert data.get('user').get('email') == expected.get('user').get('email')
    assert data.get('user').get('is_staff') == expected.get('user').get('is_staff')
    assert data.get('user').get('is_active') == expected.get('user').get('is_active')
    assert data.get('credits') == expected.get('credits')
    assert data.get('id') == expected.get('id')
