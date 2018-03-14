# Trees

A tree is a common data structure that is represented as a directed acyclic graph (DAG) in which each node, or vertex, typically contains a value (or ID) and a reference to all of its directly adjacent nodes. The reference to the adjacent nodes can be represented as a hash map, list, or a matrix depending on the specific application of the tree. Each representation of the edge set has their own pros and cons that I will discuss in detail below.

## Binary Trees

A binary tree is a common data structure that is represented as DAG where each node, or vertex, has at most 2 child nodes. Each node typically has a value stored within it and a reference to its left and right child. 


**Basic Definition (in python)**

```
class Node:
	# Constructor of the Node Class
	def __init__(self, v, l, r):
		self.value = v
		self.left = l
		self.right = r
```
