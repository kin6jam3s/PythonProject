import random


class Wizard:
    # MAGIC METHOD
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(
            self.name, creature.name
            ))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print("you roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('the wizard handily defeated {}'.format(creature.name))
            return True
        else:
            print('the wizard has been defeated!!!')
            return False


class Creature:

    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )
