class Node:
	
	def __init__(self, data):
		self.data = data
		self.lnext = None
		self.rnext = None

	def __str__(self):
		return str(self.data)


class Tree:

	def __init__(self):
		self.head = None			

	def append(self, key):
		if not self.head:
			self.head = Node(key)
		else:
			current = self.head
			while 1:
				if key < current.data:
					if current.lnext:
						current = current.lnext;
					else:
						current.lnext = Node(key)
						break;
				elif key > current.data:
					if current.rnext:
						current = current.rnext
					else:
						current.rnext = Node(key)
						break;
				else:
					break
		
	def printTree(self, node):
		if node is not None:
			self.printTree(node.lnext)
			print node.data
			self.printTree(node.rnext)


t1 = Tree()
elems = [5, 1, 4, 2, 6, 3]
for elem in elems:
	t1.append(elem)
t1.printTree(t1.head)
