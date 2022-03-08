

# node class

class Node:
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.data = data

    def insert_node(self, data):

        if self.data:
            if data < self.data:
                if self.left_child is None:
                    self.left_child = Node(data)
                else:
                    self.left_child.insert_node(data)

            else:
                if self.right_child is None:
                    self.right_child = Node(data)
                else:
                    self.right_child.insert_node(data)
        else:
            self.data = data

    # inorder traversal
    def print_tree_inorder(self):
        if self.left_child:
            self.left_child.print_tree_inorder()
        print(str(self.data) + " -> " , end='' )
        if self.right_child:
            self.right_child.print_tree_inorder()

    # preorder traversal
    def print_tree_preorder(self):

        print(str(self.data) + " -> " , end='' )
        if self.left_child:
            self.left_child.print_tree_preorder()
        if self.right_child:
            self.right_child.print_tree_preorder()

    # postorder traversal
    def print_tree_postorder(self):
        if self.left_child:
            self.left_child.print_tree_postorder()
        if self.right_child:
            self.right_child.print_tree_postorder()
        print(str(self.data) + " -> " , end='' )

root  = Node(27)
root.insert_node(11)
root.insert_node(34)
root.insert_node(16)
root.insert_node(9)
root.insert_node(67)
root.insert_node(3)
root.insert_node(55)
print("In order traversal: ")
root.print_tree_inorder()
print()
print("Pre order traversal: ")
root.print_tree_preorder()
print()
print("Post order traversal: ")
root.print_tree_postorder()