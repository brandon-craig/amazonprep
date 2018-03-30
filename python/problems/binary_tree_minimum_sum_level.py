from binarytree import Node


def levelOrderMinSum(root):
	if root is None:
		return -1

	queue = [root]
	levels = []
	while queue:
		currentLevel = []
		nextLevel = []

		while queue:
			node = queue.pop()
			currentLevel.append(node)

			if node.left:
				nextLevel.append(node.left)

			if node.right:
				nextLevel.append(node.right)

		levels.append(currentLevel)
		queue = nextLevel

	
	minLevel = None
	minSum = None
	curLevel = 0
	for level in levels:
		tempSum = 0
		curLevel += 1
		for node in level:
			tempSum += node.value

		if minSum is None or tempSum < minSum:
			minSum = tempSum
			minLevel = curLevel

	return minLevel


def main():
	root = Node(50)
	root.left = Node(18)
	root.right = Node(200)
	root.left.right = Node(100)

	print levelOrderMinSum(root)

if __name__ == '__main__':
	main()