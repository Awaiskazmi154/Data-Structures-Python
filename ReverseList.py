
# Python3 program to find middle of linked list

# single linked list node class
class Node:
    def __init__(self, data):
        self.data = data    # assign data
        self.next = None    # initialize next as null

# Single Linked List class
class LinkedList:

    # initialize head
    def __init__(self):
        self.head = None

    # insert node at the start
    def push_at_start(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # insert node at the end
    def append_at_end(self, new_data):
        new_node = Node(new_data)
        new_node.next = None

        # if list is empty
        if (self.head == None):
            self.head = new_node

        # if list is not empty
        else:
            temp = self.head

            while(temp.next):
                temp = temp.next

            temp.next = new_node


    # print the linked list
    def print_list(self):
        node = self.head
        while(node != None):
            print(str(node.data) +" -> " , end='')
            node = node.next
        print('NULL')

    # print the linked list in reverse order
    def print_list_in_reverse(self, node):

        head = node

        if head is None:
            return

        self.print_list_in_reverse(head.next)
        if head is not self.head:
            print(str(head.data) + " -> ", end='')
        else:
            print(str(head.data) + " -> NULL")

    # function to reverse a linked list
    def reverse_list(self):

        prev_node = None
        current = self.head
        next_node = current.next

        while( next_node ):

            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node

        self.head = prev_node

# Main Method
if __name__ == '__main__':

    #empty list
    list = LinkedList()

    #add nodes at start
    # for i in range(6):
    #     list.push_at_start(i+1)

    # add nodes at end
    for i in range(7):
        list.append_at_end(i + 1)

    # print list
    list.print_list()

    # reverse list
    list.reverse_list()

    # print list
    list.print_list()

    #printlist in reverse
    #list.print_list_in_reverse(list.head)