import pygame
import math
from FileManager import FileManager

pygame.init()

# Declare and generate Global Variables #
manager = FileManager()
schedule = manager.load("schedules/schedule.json")
#schedule.draw()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # if mode == schedule (show schedule)
        # if mouse on event (show name and time)
        # if mode == add event (show ui)

    pygame.display.flip()