from QueuUsingLinkedList import Queue
from BinaryTreePrinter import BinaryTreePrinter


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            nodes = Queue()
            nodes.enqueue(self.root)

            while True:
                check_node = nodes.deque()
                if check_node.left is None:
                    check_node.left = TreeNode(val)
                    return
                elif check_node.right is None:
                    check_node.right = TreeNode(val)
                    return
                else:
                    nodes.enqueue(check_node.left)
                    nodes.enqueue(check_node.right)

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)


class BST:
    def __init__(self):
        self.root = None

    def __insert_value(self, node, value):
        if node is None: return
        if node.val == value: return # this bst doesn't contain duplicate value
        elif value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
                return
            self.__insert_value(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
                return
            self.__insert_value(node.right, value)

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.__insert_value(self.root, val)

    def __find_value(self, node, value):
        if node is None:
            return -1
        if node.val == value:
            return 1
        ans = -1
        if node.val > value:
            ans = self.__find_value(node.left, value)
        else:
            ans = self.__find_value(node.right, value)
        return ans

    def find(self, val):
        return self.__find_value(self.root, val)

    def __in_order(self, node):
        if node is None: return
        self.__in_order(node.left)
        print(node.val, end=' ')
        self.__in_order(node.right)

    def in_order(self):
        self.__in_order(self.root)

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)


# my_tree = BinaryTree()
# for i in [1, 2, 3, 6, 7, 12, 45, 54, 12, 45, 76, 33, 12, 11, 101]:
#     my_tree.insert(i)
#     print(my_tree)
#
# bst = BST()
# for i in [8, 2, 1, 10, 100, 50, 40, 23, 16, 7, 9, 200, 150, 300]:
#     bst.insert(i)
# print(bst)
#     print(bst)
# while True:
#     n = int(input('Enter a number: '))
#     if bst.find(n) == -1:
#         print('The number not found')
#     else:
#         print('Number is found')
# bst.in_order() # print the number in accending order
