import pygame
from pygame import gfxdraw
import math
import time

from InteractiveScreen import InteractiveScreen
from FileManager import FileManager

pygame.init()

state = 0
states = []

# Declare and generate Global Variables #
#manager = FileManager()
# How about we build the schedule with an 'InteractiveScreen' and for the special characteristics it has,
# Like double click
#states.append(manager.load("schedules/schedule.json"))

#mainMenu = InteractiveScreen()
			    #   Rectangle info,   button color, label,  labelLoc, size, stateTo
#mainMenu.addButton((50, 50, 25, 25), [60, 60, 130], "Load", (50, 40), 10, 1)  
running = True
done = False
while running and not done:
	# Query pygame for events #
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	###########################

	##### Active draw loop ####

	#states[state].draw()

	###########################

	###### Update display #####
	pygame.display.flip()
	###########################
