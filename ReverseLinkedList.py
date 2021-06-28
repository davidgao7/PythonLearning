class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def ReverseList(pHead):
	
	if not pHead:
		return None # empty linked list
	
	root = None
	
	while pHead:
		pHead.next, root, pHead = root, pHead, pHead.next
		"""
		same as:
		temp = pHead.next
		pHead.next = root
		root = pHead
		pHead = temp
		"""
	return root

"""
TEST
"""
def printList(node):
	if (node is not  None):
		print(node.val)
		printList(node.next)

node0 = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node0.next = node1
node1.next = node2

print("original linked list:")
#printList(node0)
print(node0.__dict__)
print("reverse:")
#printList(ReverseList(node0))
print(ReverseList(node0).__dict__)
