import pygame

class InteractiveScreen:           # Object from which all user interaction is built from
	screenWidth, screenHeight = 430, 400
	screen = pygame.display.set_mode((screenWidth, screenHeight))
	screen.fill([38, 35, 30]) 				# redundant
	
	def __init__(self):						# The constructor
		self.base = [0, 0, 0]				# Every screen has a base color
		
	def draw(self):
		self.screen.fill(self.base)

	class Button:
		def __init__(self):
			self.rectDat = (0, 0, 0, 0)     # Data of starting point, width, and height
			self.label = ""                 # What the button says
			self.labelLoc = ()              # Where the label apears
		def isClicked(self):
			return
		def draw(self):
			return
        

