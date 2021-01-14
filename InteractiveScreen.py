import pygame

class InteractiveScreen:  # Object from which all user interaction is built from
	screenWidth, screenHeight = 430, 400
	screen = pygame.display.set_mode((screenWidth, screenHeight))
	screen.fill([38, 35, 30])  # redundant

	class Button:
		def __init__(self, rectDat, color, label, labelLoc, size, stateTo):
			self.rectDat = (rectDat[0] * InteractiveScreen.screenWidth,
							rectDat[1] * InteractiveScreen.screenHeight,
							rectDat[2] * InteractiveScreen.screenWidth,
							rectDat[3] * InteractiveScreen.screenHeight)  # Data of starting point, width, and heightself.color = [100, 25, 25]
			self.color = color
			self.label = label  # What the button says
			self.labelLoc = labelLoc  # Where the label apears
			self.labelSize = size
			self.stateTo = stateTo

		def isClicked(self, mouseX, mouseY):
			return

		def draw(self):
			pygame.rect.draw(InteractiveScreen.screen, self.color, self.rectDat)
			InteractiveScreen.draw_text(self.label, self.labelLoc, self.labelSize)

	def __init__(self):			# The constructor
		self.base = [0, 0, 0]  # Every screen has a base color
		self.Buttons = []      # Every button which the screen has
		self.drawables = []    # This should include anything that shoudld be drawn, text, cosmetics, etc.

	def draw(self):
		self.screen.fill(self.base) # What about buttons explicitly?
		for object in self.drawables:
			object.draw()

	def draw_text(text, location, size):
		font = pygame.font.SysFont("comicsansms", size)
		textObject = font.render(text, True, (200, 200, 200))
		InteractiveScreen.screen.blit(textObject, location)
		
	def addButton(self, rectDat, color, label, labelLoc, size, stateTo):
		self.drawables.append(self.Button(rectDat, color, label, labelLoc, size, stateTo))


