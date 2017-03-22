#import actors
import PYTHON_PROJ_7_1

def main()
	print_header()
	game_loop()

	
	
def print_header():
	print'------------------------------')
	print'      Wizard Battle APP')
	print'------------------------------')
	print()
	
	

		
	
def game_loop():

	creatures = [
		Creature('Toad', 1),
		Creature('Tiger', 12),
		Creature('Bat', 3),
		Creature('Dragon', 50),
		Creature('Evil Wizard', 1000),
	]
	
	# print(Creature)
	
		hero = Wizard('Gandolf', 75)
		

	while True:
	
		active_creature = random.choice(creature)
		print ('A {} of a level {} has appear from a dark and foggy forest..'
				.format(active_creature.name, active_creature.level))
			
		print()
	
	
		cmd = input ('Do you [a]ttack, [r]unaway, or [l]ookaround')
			if cmd = 'a':
				print('attack')
				if hero.attack(active_creature):
					creature.remove(active_creature)
				else:
					print("the wixard runs and hides taking time to recover..")
					time.sleep(5)
					print("The wizard return revitalized!")
				
			elif cmd = 'r':
				print('The wizard becomes unsure of his powers and flees')
			elif cmd = 'l':
				print('the wizard {} takes in the surrounding and sees:'.format(hero.name))
				for c in creature
					print(' * A {} of level {}.format.(creature.name, creature.level))
			else:
				print('sorry invalid input')
				break
			
			print()
			
				
			


if __name__ == '__main__':
	main()
	