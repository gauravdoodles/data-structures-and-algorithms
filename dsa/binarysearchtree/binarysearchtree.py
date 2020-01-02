class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
class BinaryTree:
	def __init__(self):
		self.root=None
	def insert(self,data):
		if self.root is None:
			self.root=Node(data)
		else:
			self._insert(data,self.root)
	
	def _insert(self,data,cur_node):
		if data<cur_node.data:
			if cur_node.left is None:
				cur_node.left=Node(data)
			else:
				self._insert(data,cur_node.left)
		else:
			if data > cur_node.data:
				if cur_node.right is None:
					cur_node.right=Node(data)
				else:
					self._insert(data,cur_node.right)

	def preorder_print(self,start):
		if start:
			print(start.data)
			self.preorder_print(start.left)
			self.preorder_print(start.right)


bt=BinaryTree()
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)
bt.preorder_print(bt.root)

