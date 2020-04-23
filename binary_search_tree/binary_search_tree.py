from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current = self
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BinarySearchTree(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = BinarySearchTree(value)
                    break
                else:
                    current = current.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = self
        while True:
            if target == current.value:
                return True
            elif target < current.value:
                if current.left:
                    current = current.left
                else:
                    return False
            else:
                if current.right:
                    current = current.right
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while True:
            if not current.right:
                return current.value
            else:
                current = current.right

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
        cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        current = node if node else self
        if current.left:
            current.left.in_order_print(current.left)
        print(current.value)
        if current.right:
            current.right.in_order_print(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            next = q.dequeue()
            print(next.value)
            if next.left:
                q.enqueue(next.left)
            if next.right:
                q.enqueue(next.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
            next = stack.pop()
            print(next.value)
            if next.right:
                stack.push(next.right)
            if next.left:
                stack.push(next.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.dft_print(bst)
