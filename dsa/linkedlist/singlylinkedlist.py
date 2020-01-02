class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class linked_list:
	def __init__(self):
		self.head=None
	def append(self,data):
		new_node=node(data)
		if self.head is None:
			self.head=new_node
			return
		last_node=self.head
		while last_node.next:
			last_node=last_node.next
		last_node.next=new_node
	def print_list(self):
		curr=self.head
		while curr:
			print(curr.data)
			curr=curr.next
	def preappend(self,data):
		new_node=node(data)
		new_node.next=self.head
		self.head=new_node
	def insert_node_after(self,prev_node,data):
		if not prev_node:
			print("node does not exist")
		new_node=node(data)
		
		new_node.next=prev_node.next
		prev_node.next=new_node
	def delete(self,key):
		prev=None
		after=self.head
		if after.data==key:
			self.head=after.next
			after=None
			return

		while after.data!=key and after :
			prev=after
			after=after.next

		prev.next=after.next
		after=None



ll=linked_list()
ll.append(1)
ll.append(2)
ll.append(3)
ll.preappend(4)
ll.insert_node_after(ll.head.next,10)

ll.delete(4)

ll.print_list()

