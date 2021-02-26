import json

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def serialize(root):
	if not root:
		return None

	treeString = dict()

	treeString['value'] = root.val

	leftChild = serialize(root.left)
	rightChild = serialize(root.right)

	if leftChild:
		treeString['left'] = leftChild
	if rightChild:
		treeString['right'] = rightChild

	return json.dumps(treeString)


def deserialize(d):
	tree = json.loads(d)

	node = Node(tree['value'])

	if 'left' in tree:
		node.left = deserialize(tree['left'])
	if 'right' in tree:
		node.right = deserialize(tree['right'])

	return node

##########################
node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')
node5 = Node('e')
node6 = Node('f')
node7 = Node('g')
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7


serTree = serialize(node1)
print(serTree)
deserTree = deserialize(serTree)
assert deserTree.left.val == node1.left.val