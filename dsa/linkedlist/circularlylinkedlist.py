class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class CircularLinkedList:
	def __init__(self):
		self.head=None
	def append(self,data):
		new_node=Node(data)
		if not self.head:
			self.head=new_node
			self.head.next=self.head
		else:
			curr=self.head
			while(curr.next!=self.head):
				curr=curr.next
			curr.next=new_node
			new_node.next=self.head
	def preappend(self,data):
		new_node=Node(data)
		curr=self.head
		new_node.next=self.head
		if not self.head:
			new_node.next=new_node
		else:
			while curr.next!=self.head:
				curr=curr.next
			curr.next=new_node

		self.head=new_node

	def remove(self,key):
		if self.head.data==key:
			curr=self.head
			while curr.next!=self.head:
				curr=curr.next
			curr.next=self.head.next
			self.head=self.head.next
		else:
			prev=None
			curr=self.head
			while curr.next!=self.head:
				prev=curr
				curr=curr.next
				if curr.data==key:
					prev.next=curr.next
					curr.next

	def printlist(self):
		curr=self.head
		while curr:
			print(curr.data)
			curr=curr.next
			if curr==self.head:
				break

cll=CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.preappend(4)
cll.remove(2)
cll.remove(1)
cll.remove(4)
cll.remove(3)
cll.printlist()