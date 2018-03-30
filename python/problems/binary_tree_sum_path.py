from binarytree import Node

def printPath (path):
	if path is None:
		print "Path is empty"
		return

	print "PATH:",
	for i, node in enumerate(path):
		if not i == (len(path) - 1):
			print "{} ->".format(node.value),
		else:
			print node.value


def dfs (node, k, psum=0, path=[]):
	if node is None:
		return

	path.append(node)
	psum += node.value

	if psum == k:
		printPath(path)

	pathLeft = list(path)
	pathRight = list(path)

	dfs(node.left, k, psum, pathLeft)
	dfs(node.right, k, psum, pathRight)

def main():
	print "Starting main function"
	root = Node(1)
	root.left = Node(1)
	root.right = Node(2)
	root.left.right = Node(1)

	dfs(root, 3)

if __name__ == '__main__':
	main()

