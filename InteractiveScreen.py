import pygame

class InteractiveScreen:  # Object from which all user interaction is built from
	screenWidth, screenHeight = 800, 540
	screen = pygame.display.set_mode((screenWidth, screenHeight))
	screen.fill([38, 35, 30])  # redundant

	class Button:
		def __init__(self, rectDat, color, label, labelLoc, size, labelColor, stateTo):
			self.rectDat = (rectDat[0] / 100 * InteractiveScreen.screenWidth,
							rectDat[1] / 100 * InteractiveScreen.screenHeight,
							rectDat[2] / 100 * InteractiveScreen.screenWidth,
							rectDat[3] / 100 * InteractiveScreen.screenHeight)  # Data of starting point, width, and heightself.color = [100, 25, 25]
			self.color = color
			self.label = label  # What the button says
			self.labelLoc = (labelLoc[0] / 100 * InteractiveScreen.screenWidth, 
							 labelLoc[1] / 100 * InteractiveScreen.screenHeight)  # Where the label apears
			self.labelSize = round(size / 100 * InteractiveScreen.screenHeight)
			self.labelColor = labelColor
			self.stateTo = stateTo

		def isClicked(self, mousePosition):
			return

		def draw(self):
			pygame.draw.rect(InteractiveScreen.screen, self.color, self.rectDat)
			InteractiveScreen.draw_text(self.label, self.labelLoc, self.labelSize, self.labelColor)

	def __init__(self):			# The constructor
		self.base = [0, 0, 0]  # Every screen has a base color
		self.Buttons = []      # Every button which the screen has
		self.drawables = []    # This should include anything that shoudld be drawn, text, cosmetics, etc.

	def draw(self):
		self.screen.fill(self.base) # What about buttons explicitly?
		for object in self.drawables:
			object.draw()

	def draw_text(text, location, size, color):
		font = pygame.font.Font("Fonts/Dense.otf", size) # minimalist font
		textObject = font.render(text, True, color)
		# After creating the text Object, get the dimensions of it
		textRect = textObject.get_rect()
		location = (location[0] - textRect.width/2, location[1] - textRect.height/2)
		InteractiveScreen.screen.blit(textObject, location)
		
	def addButton(self, rectDat, color, label, labelLoc, size, labelColor, stateTo):
		self.drawables.append(self.Button(rectDat, color, label, labelLoc, size, labelColor, stateTo))


