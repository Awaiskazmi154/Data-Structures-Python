
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

    # function return the middle of list => Using fast and slow pointers
    def middle_of_list_using_fast_slow_pointers(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while( fast_pointer and fast_pointer.next ):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            print("The middle of the list is "+ str(slow_pointer.data))

    # function return the middle of list => Using odd counter
    def middle_of_list_using_odd_counter(self):
        counter = 0
        temp = self.head
        mid = self.head

        while (temp):

            if (counter % 2 == 1):
                mid = mid.next

            temp = temp.next
            counter = counter + 1

        print("The middle of the list is " + str(mid.data))

    # find the middle of the list => using the count/2
    def find_middle_of_list_using_nodes_count(self):
        nodes = 0
        temp = self.head

        while(temp):
            nodes = nodes + 1
            temp = temp.next

        temp = self.head
        count = nodes/2

        while(count > 1):
            temp = temp.next
            count = count - 1

        print("The middle of the list is " + str(temp.data))


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

    #printlist
    list.print_list()

    #find middle using fast slow pointers
    #list.middle_of_list()

    # find mid using odd counter
    #list.middle_of_list_using_odd_counter()

    # find mid using half nodes count
    list.find_middle_of_list_using_nodes_count()



