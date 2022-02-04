from random import choice, randint
from apps.jack_app.models import Fruit


class JackPotService():

    def __init__(self):
        self.fruits = Fruit.objects.all()

    def get_new_roll(self, current_credits):
        new_roll = self.generate_roll()
        while new_roll.count(new_roll[0]) == 3 and self.re_roll(current_credits):
            new_roll = self.generate_roll()
        new_credit = new_roll[0].value if new_roll.count(new_roll[0]) == 3 else -1
        new_roll = [r.id for r in new_roll]
        return new_roll, new_credit

    def generate_roll(self):
        roll = []
        for f in range(3):
            roll.append(choice(self.fruits))
        return roll

    def re_roll(self, current_credits):
        chance = 0
        if 40 <= current_credits <= 60:
            chance = 30
        elif 60 < current_credits:
            chance = 60
        random_number = randint(1, 100)
        res = random_number <= chance
        return res

