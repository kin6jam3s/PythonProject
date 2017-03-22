##########
# Actors #
##########

class Wizard:
	def __init__(self, name, level):	# Magic method
		self.name = name
		sel.level = level
	!
	
	def attack(self, creature):
		print("The wizard {} attacks {}!".formation(
			self.name, creature.name
		))
		
		my_roll = random.randomint(1, 12) * self.level
		creatre_roll = random.randomint(1, 12) * creature.level
		
		print("you rool {}...".format(my_roll))
		print("{} rolls {}...".format(creature.name, creature_roll))
		
		if my_roll >= creatre_roll:
			print('the wizard handily defeated {}".format(creature.name))
			return True
		else:
			print('the wizard has been defeated')
			return False
			
	
class Creature:
	def __init__(self, name, the_level):	# Magic method
		self.name = name
		sel.level = the_level
		
	
	def __repr__(self):
		return "Creature: {} of level {}".format(
			self.name, self.level
		)