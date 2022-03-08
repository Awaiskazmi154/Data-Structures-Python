
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

# function merge values from two lists, sum them and generate new list as separate values
def merge_list_values_sum_lists_generate_new_list(list1_head, list2_head):

    temp = list1_head
    merged_value_lst_1 = 0
    while (temp):
        # 3  * 10 -> (30 + 2) * 10 -> (320 + 1)  * 10 -> 3210
        merged_value_lst_1 = (temp.data + merged_value_lst_1) * 10
        temp = temp.next

    merged_value_lst_1 = merged_value_lst_1 / 10

    temp = list2_head
    merged_value_lst_2 = 0
    while (temp):
        # 1  * 10 -> (10 + 7) * 10 -> (170 + 2)  * 10 -> 1720
        merged_value_lst_2 = (temp.data + merged_value_lst_2) * 10
        temp = temp.next

    merged_value_lst_2 = merged_value_lst_2 / 10

    sum = merged_value_lst_1 + merged_value_lst_2

    # initialize new list
    list_3 = LinkedList()

    while (sum > 1):
        # 493 = 571 % 10 -> 1 and 571 / 10 = 57

        list_3.push_at_start(int(sum % 10))
        sum = sum / 10

    return list_3



# Main Method
if __name__ == '__main__':

    #empty list
    list_1 = LinkedList()
    list_2 = LinkedList()

    list_1.append_at_end(3)
    list_1.append_at_end(2)
    list_1.append_at_end(1)
    print("List 1 is: ")
    list_1.print_list()

    list_2.append_at_end(1)
    list_2.append_at_end(7)
    list_2.append_at_end(2)
    print("List 2 is: ")
    list_2.print_list()

    list_3 = merge_list_values_sum_lists_generate_new_list(list_1.head, list_2.head)

    #printlist
    print("New List is: ")
    list_3.print_list()




