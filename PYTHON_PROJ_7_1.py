import random

#

class Creature:

    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    # MAGIC METHOD
    # def __init__(self, name, level):
    #     super.__init__(name, level)
        # self.name = name
        # self.level = level

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(
            self.name, creature.name
            ))

        my_roll = self.get_defensive_roll()
        #creature_roll = random.randint(1, 12) * self.level
        creature_roll = creature.get_defensive_roll()

        print("you roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('the wizard handily defeated {}'.format(creature.name))
            return True
        else:
            print('the wizard has been defeated!!!')
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        print("base_roll is {}".format(base_roll))
        return base_roll/2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_role = super().get_defensive_roll()
        # fire_modifier = None
        # if self.breaths_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1
        #
        # fire_modifier = VALUE_IF_TRUE if SOME TEST else VALUE_IF_FALSE
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10
        print("Fire Modifier: {} ".format(fire_modifier))
        print("Scale Modifier: {} ".format(scale_modifier))
        print("Base Role: {} ".format(base_role))

        return base_role * fire_modifier * scale_modifier
