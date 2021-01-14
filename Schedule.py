from Event import Event
from InteractiveScreen import InteractiveScreen

class Schedule(InteractiveScreen):
	pass
	def __init__(self, data):

		# Inherit variables defined in parents init function #
		InteractiveScreen.__init__(self)

		self.name = data["name"]
		self.isMilitary = False
		self.events = []

		for x in data["events"]:
			self.events.append(Event(data["events"][x]))
			
	def getDict(self):
		eventDicts = []

		for x in self.events:
			eventDicts.append(x.getDict())
		
		return {"name": self.name, "military": self.isMilitary, "events": eventDicts}
