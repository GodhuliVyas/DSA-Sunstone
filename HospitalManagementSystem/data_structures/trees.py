class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key, value)
            else:
                self._insert(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key, value)
            else:
                self._insert(node.right, key, value)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def in_order_traversal(self):
        nodes = []
        self._in_order_traversal(self.root, nodes)
        return nodes

    def _in_order_traversal(self, node, nodes):
        if node:
            self._in_order_traversal(node.left, nodes)
            nodes.append(node.value)
            self._in_order_traversal(node.right, nodes)

class PatientTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

class AppointmentTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
