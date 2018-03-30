from collections import defaultdict

class Graph:
	def __init__(self):
		self.vertexes = set()
		self.edges = defaultdict(list)

	def addVertex(self, vertex):
		self.vertexes.add(vertex)

	def addEdge(self, i, j):
		self.addVertex(i)
		self.addVertex(j)
		self.edges[i].append(j)

