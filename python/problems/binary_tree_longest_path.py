from binarytree import Node, printPath

def longest_path(node):
	if node is None:
		return None

	path = [node]
	result = getMaxPath(longest_path(node.left), longest_path(node.right))

	if result is not None:
		path.extend(result)

	return path


def getMaxPath(left, right):
	if left is None and right is None:
		return None

	if left is None:
		return right

	if right is None:
		return left

	if len(left) > len(right):
		return left
	else:
		return right


def main():
	print "Computing Longest Path"
	root = Node(1)
	root.left = Node(1)
	root.right = Node(2)
	root.left.right = Node(1)

	printPath(longest_path(root))


if __name__ == '__main__':
	main()