class Node:
	def __init__(self, v):
		self.value = v
		self.left = None
		self.right = None

def printPath (path):
	if path is None or len(path) == 0:
		print "Path is empty"
		return

	print "PATH:",
	for i, node in enumerate(path):
		if not i == (len(path) - 1):
			print "{} ->".format(node.value),
		else:
			print node.value