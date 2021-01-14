import pygame
from pygame import gfxdraw
import math
import time
from InteractiveScreen import InteractiveScreen
#from FileManager import FileManager

#time.sleep(10)
#screen = pygame.display.set_mode((400, 400))
#screen.fill([38, 35, 30])
pygame.init()

state = "Main Menu"
states = {} # Use a dictionary so that we can say 'Jump to "Main Menu"'

# Declare and generate Global Variables #
#manager = FileManager()
# How about we build the schedule with an 'InteractiveScreen' and for the special characteristics it has,
# Like double click
#states.append(manager.load("schedules/schedule.json"))
print("About to make screen")
states["Main Menu"] = InteractiveScreen()
						   #   Lets have the 'labelLoc' Specify where we want the center of the label to be
			               #   Rectangle info,  button color, label,  labelLoc, size, labelColor, stateTo
states["Main Menu"].addButton((55, 25, 40, 50), [232, 129, 52], "LOAD", (75, 50), 20, (247, 246, 225), "Load")  
states["Main Menu"].addButton((5, 25, 40, 50), [232, 129, 52], "CREATE", (25, 50), 20, (247, 246, 225), "Create")
states["Main Menu"].base = [4, 35, 48]



running = True
done = False
while running and not done:
	# Query pygame for events #
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	###########################

	##### Active draw loop ####

	states[state].draw()

	###########################

	###### Update display #####
	pygame.display.flip()
	########################, ###
