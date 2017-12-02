# Python program to find predecessor and successor in a BST

# A BST node
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# A utility function to insert a new node in with given key in BST
def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


# fs(50) - 50, fs(30)
#					fs(30) - 80, fs(20)
#									fs(20) - 100

def find_sum(root):
    if root is None:
        return 0
    return root.key + find_sum(root.left) + find_sum(root.right)

def print_tree(root):
    if root is None:
        return
    else:
        left = str(root.left.key) if root.left is not None else "NULL"
        right = str(root.right.key) if root.right is not None else "NULL"
        print str(root.key) + " : left->{left} , right->{right}".format(left=left, right=right)
    print_tree(root.left)
    print_tree(root.right)
# Driver program to test above function

""" Let us create following BST
		50
	 /		\
	30		70
	/ 	\   / 	\
	20 	40	60 	80
"""
root = None
root = insert(root, 50)
insert(root, 30);
insert(root, 20);
insert(root, 40);
insert(root, 70);
insert(root, 60);
insert(root, 80);

print "Sum of all nodes is", find_sum(root)
#print_tree(root)