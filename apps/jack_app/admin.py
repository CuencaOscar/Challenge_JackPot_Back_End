from django.contrib import admin

from apps.jack_app.models import Fruit, CreditUser

# Register your models here.
admin.site.register(Fruit)
admin.site.register(CreditUser)