from Schedule import Schedule
import json

class FileManager:
	def save(self, path):
		with open(path, "w") as file:
			json.dump(self.active.getDict(), path)
		file.close()

	def load(self, path):
		with open(path, "r") as file:
			return Schedule(json.load(file))
		file.close()