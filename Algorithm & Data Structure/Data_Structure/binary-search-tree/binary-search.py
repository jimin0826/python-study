class Node() :
    def __init__(self, data) :
        self.data = data
        self.left = self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def search(self, key) :
        return self._search(key, self.root)

    def _search(self, data, node) :
        if node is None :
            return False
        elif data == node.data :
            return True
        else :
            if data > node.data :
                return self._search(data, node.right)
            else :
                return self._search(data, node.left)

    def add(self, data):
        self.root = self.add_val(self.root, data)
        return self.root is not None

    def add_val(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self.add_val(node.left, data)
            else:
                node.right = self.add_val(node.right, data)
        return node

    def delete(self, key):
        self.root, deleted = self.del_v(self.root, key)
        return deleted

    def del_v(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right

                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left

                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None

        elif key < node.data:
            node.left, deleted= self.del_v(node.left, key)
        else:
            node.right,deleted=self.del_v(node.right,key)
        return node, deleted

def preorder_traverse(tree):
    if tree == None: return
    print(tree.data)
    preorder_traverse(tree.left_child)
    preorder_traverse(tree.right_child)

def inorder_traverse(tree):
    if tree == None: return
    inorder_traverse(tree.left_child)
    print(tree.data)
    inorder_traverse(tree.right_child)

def postorder_traverse(tree):
    if tree == None: return
    postorder_traverse(tree.left_child)
    postorder_traverse(tree.right_child)
    print(tree.data)