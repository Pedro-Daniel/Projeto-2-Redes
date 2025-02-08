
class Node:
	def __init__(self):
		self.name = ""
		self.neighbors = {
			# neighbor name : neighbor edge weight
			"" : 0
		}

	def access_neighbors(self):
		for neighbor in self.neighbors:
			pass
