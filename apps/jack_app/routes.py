from django.urls import path
from apps.jack_app.views import AuthenticationViewSet, JackPotViewSet


urlpatterns = [
    path('', JackPotViewSet.as_view({'get': 'list'}), name='data_list'),
    path('user/', JackPotViewSet.as_view({'get': 'user'}), name='user_list'),
    path('new_roll/', JackPotViewSet.as_view({'post': 'new_roll'}), name='new_roll'),
    path('auth/', AuthenticationViewSet.as_view({'post': 'sign_up'}, name='auth')),
]