class Event:
	week = ['S', 'M', 'T', 'W', 'R', 'F', 'A']

	def __init__(self, eventDat):
		if type(eventDat) == dict:
			self.name = eventDat["name"]
			self.daysOfWeek = eventDat["days"]
			self.startTime = eventDat["start"]
			self.eventLength = eventDat["length"]
			self.color = eventDat["color"]
		if type(eventDat) == str:
			stringList = eventDat.split(' ')
			self.name = stringList[0].replace('_', ' ')
			self.daysOfWeek = [0] * 7
			for c in stringList[1]:
				self.daysOfWeek[Event.week.index(c)] = 1
			self.startTime, endTime = [
				self.strTimeToNum(temp) for temp in stringList[2][:].split('-')
			]
			self.eventLength = endTime - self.startTime
			self.color = [
				int(stringList[3]),
				int(stringList[4]),
				int(stringList[5])
			]

	def strTimeToNum(self, line: str):  # 09:15AM
		total = int(line[0:2]) % 12 * 60 + int(line[3:5])
		if line[5:7] == "PM":
			total += 720
		return total

	def getDict(self):
		return {
			"name": self.name,
			"days": self.daysOfWeek,
			"start": self.startTime,
			"length": self.eventLength,
			"color": self.color
		}

	def printDat(self):
		print(self.name)
		print(self.daysOfWeek)
		print(self.startTime)
		print(self.eventLength)
		print(self.color)

