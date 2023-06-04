class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.bst_insert(self.root, new_val)

    def search(self, find_val):
        if self.bst_search(self.root, find_val):
            return True
        return False

    def print_tree(self):
        tree = []
        tree = self.bst_print(self.root, tree)
        return tree

    def bst_insert(self, root, new_val):
        if new_val < root.value:
            if root.left:
                self.bst_insert(root.left, new_val)
            else:
                root.left = Node(new_val)
        else:
            "Assuming no duplicates"
            if root.right:
                self.bst_insert(root.right, new_val)
            else:
                root.right = Node(new_val)

    def bst_search(self, root, find_val):
        if root.value == find_val:
            return True
        elif root.value < find_val:
            if root.left:
                self.bst_search(root.left, find_val)
        else:
            if root.right:
                self.bst_search(root.right, find_val)

        return False

    def bst_print(self, root, tree):
        if root.left:
            "Let the left node manage it's own thing"
            tree = self.bst_print(root.left, tree)

        "Once it's done, I'll add my value"
        tree.append(root.value)

        "Before checking if there is a right node"
        if root.right:
            tree = self.bst_print(root.right, tree)

        return tree


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print(tree.print_tree())

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
