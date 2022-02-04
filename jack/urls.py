from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('JackPot/', include('apps.jack_app.routes'))
]
