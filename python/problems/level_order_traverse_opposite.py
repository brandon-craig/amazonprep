from binarytree import Node

def levelOrderTraversal(root):
	if root is None:
		return []

	result = []
	queue = [root]

	while queue:
		tempList = []
		qSize = len(queue)

		for i in range(qSize):
			temp = queue.pop(0)
			tempList.append(temp.value)
			if temp.right:
				queue.add(temp.right)
			if temp.left:
				queue.add(temp.left)

		result.append(tempList)

	return result


def main():
	pass

if __name__ == '__main__':
	main()