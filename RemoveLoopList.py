
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

    # detect loop in single linked list => using fast and slow pointers
    def detect_and_remove_loop(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while( slow_pointer and fast_pointer and fast_pointer.next):

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if ( slow_pointer == fast_pointer):
                print( "The loop node is : " + str(slow_pointer.data))
                ptr1 = slow_pointer
                ptr2 = slow_pointer
                nodes = 1
                #count nodes
                while ( ptr1.next != ptr2):

                    ptr1 = ptr1.next
                    nodes += 1

                print("Number of nodes in the loop : " + str(nodes))
                temp = slow_pointer.next
                while( nodes > 1):
                    temp = temp.next
                    nodes = nodes - 1

                temp.next = None

                return


    # detect loop in single linked list => using fast and slow pointers (optimized)
    def detect_and_remove_loop_Optimized(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while( slow_pointer and fast_pointer and fast_pointer.next):

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if ( slow_pointer == fast_pointer):
                print( "The loop node is : " + str(slow_pointer.data))
                slow_pointer = self.head

                while ( slow_pointer.next != fast_pointer.next):

                    slow_pointer = slow_pointer.next
                    fast_pointer = fast_pointer.next

                fast_pointer.next = None
                return

# Main Method
if __name__ == '__main__':

    #empty list
    list = LinkedList()

    #add nodes at start
    # for i in range(6):
    #     list.push_at_start(i+1)

    # add nodes at end
    for i in range(5):
        list.append_at_end(i + 1)

    #printlist
    list.print_list()

    # create a loop in the list

    # 1 -> 2 -> 3 -> 4 -> 5 - >
    #      ^                  |
    #      |-------------------

    list.head.next.next.next.next.next = list.head.next

    # remove the loop from list using slow and fast pointers
    # list.detect_and_remove_loop()

    # remove the loop from list using slow and fast pointers
    list.detect_and_remove_loop_Optimized()

    # printlist
    list.print_list()



