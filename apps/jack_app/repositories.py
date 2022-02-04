from apps.jack_app.models import Fruit, CreditUser


class JackPotRepository():
    def getFruit(self):
        return Fruit.objects.all()
    
    def getCreditUSer(self):
        return CreditUser.objects.all()