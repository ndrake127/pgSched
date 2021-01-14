import pygame
import math
from FileManager import FileManager
from Schedule import Schedule

pygame.init()

# Declare and generate Global Variables #
manager = FileManager()
schedule = FileManager.load("../schedules/schedule.json")


screenWidth, screenHeight = 430, 400
dayWidths, dayStarts = [], [0]

for i in range(7):  # For
    dayWidths.append(max(0, math.floor((screenWidth - i) / 7)))

for i in range(6):
    dayStarts.append(dayStarts[-1] + 1 + dayWidths[i])

grey = [38, 35, 30]
#########################################

# Open file
data = open("AlexanderClasses.txt", "r")

screen = pygame.display.set_mode((screenWidth, screenHeight))
screen.fill(grey)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # if mode == schedule (show schedule)
        # if mouse on event (show name and time)
        # if mode == add event (show ui)

    pygame.display.flip()