# Trees

A tree is a common data structure that is represented as a directed acyclic graph (DAG) in which each node, or vertex, typically contains a value (or ID) and a reference to all of its directly adjacent nodes. The reference to the adjacent nodes can be represented as a hash map, list, or a matrix depending on the specific application of the tree. Each representation of the edge set has their own pros and cons that I will discuss in detail below.

## Binary Trees

A binary tree is a common data structure that is represented as a DAG where each node, or vertex, has at most 2 child nodes. Each node typically has a value stored within it and a reference to its left and right child. 


Basic Definition (in python)

```
class Node:
	# Constructor of the generic Node class
	def __init__(self, v, l, r):
		self.value = v
		self.left = l
		self.right = r
```

### Binary Search Trees

A binary search tree (BST) is a specialized binary tree in which each node has an integer value. The value of each parent node is greater-than or equal-to the values of all of its left-side children and the value of the parent node is less-than or equal-to the value of all of its right-side children.

Example BST
```
     5
   /   \
  3     7
 / \     \
2   4     9

```

Basic definition and required function outlines for a BST Node in python that inherits from the `Node` class that was defined above.

```
class BSTNode (Node):

	# Inserts value into BST
	def insert (self, v):
		pass

	# delete value from BST
	def delete (self, v):
		pass

	# Searches BST for a specified value
	def search (self, v):
		pass
```

**Search**

Searching a BST for a specified value on average takes **O(log n)** time, where n is the number of nodes in the BST. This performance is due to the specialized nature of a BST that was outlined above. 

Example recursive search function of a BST

```
def search (self, v):

	# Check if we found the value. If so, return True
	if self.value == v:
		return True

	# Check if the search value is less-than the current value.
	# If yes and we have a left child, then search the left child for the specified value.
	if self.value < v and self.left is not None:
		return self.search(self.left, v)

	# Check if the search value is greater-than the current value.
	# If yes and we have a right child, then search the right child for the specified value.
	elif self.value > v and self.right is not None:
		return self.search(self.right, v)

	# Since we ran out of nodes/values to search through
	# the value must not exist in the BST.
	# Thus, we return False
	else:
		return False
```

This recursive search function will at-most visit any node once, meaning the worst cast run-time of this function is **O(n)**.

**Insertion**

Inserting a value into a BST is, at it's core, a search operation to find the proper location in which to place the specified value. Being that the insert function is based on the search function, the run-time is on average the same as search, meaning **O(log n)**.

Example insert function for a BST with right-side bias for values that are equal to the root's value

```
def insert (self, v):
	
	# Check if root's value is less-than or equal-to the specified value
	if self.value == v or self.value < v:

		# If the right child is None, then we found the location we want to insert the value to
		# Set the right child equal to a new BSTNode with value v
		if self.right is None:
			self.right = BSTNode(v)

		# If the right child is not None, then we need to keep searching
		# Recursively call insert on the right child in order to find the proper location
		# as we know the proper location must be to the right
		else:
			self.insert(self.right, v)

	# At this point, we know the value of v is less than the root's value
	else:
		# If the left child is None, then we found the location we want to insert the value to
		# Set the left child equal to a new BSTNode with value v
		if self.left is None:
			self.left = BSTNode(v)

		# If the left child is not None, then we need to keep searching
		# Recursively call insert on the left child in order to find the proper location
		# as we know the proper location must be to the left
		else:
			self.insert(self.left, v)

```

This recursive insert functions works by traversing the tree looking for the first location that maintains the BST property stated above, and inserts the value at that location.

**Deletion**

```
def delete (self, v):
	pass
```