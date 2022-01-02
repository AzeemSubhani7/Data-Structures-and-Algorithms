# Linked lists in python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion At the Beginning
    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    # Insert After a Node
    def insertAtPosition(self, position, data):
        cursor = self.head
        i = 0
        while( i < position - 2):
# i start from 0 and pos - 2 i'll have the pos - 1th element means 5 input and will have 4th node
            cursor = cursor.next
            i = i + 1

        # newNode.next = cursor.next
        # print(cursor.data, "Insert Here")
        newNode = Node(data)
        newNode.next = cursor.next
        cursor.next = newNode
    # Insertion At the End
    def append(self, data):
        new_node = Node(data)
        # Checking is List is empty
        if self.head is None:
            self.head = new_node
            return
        cursor = self.head
        while(cursor.next != None):
            cursor = cursor.next
        # Traversing till the last
        cursor.next = new_node

    # Printing The List
    def printList(self):
        cursor = self.head
        while cursor:
            print(cursor.data, '--> ', end='')
            cursor = cursor.next

    # Deletion of a node
    def deleteByData(self, key):
        cursor = self.head
        # If head value is the value to delete
        if cursor and cursor.data == key:
            self.head = cursor.next
            cursor = None

        prev = None
        while cursor and cursor.data != key:
            prev = cursor
            cursor = cursor.next
        # If cursor is None the the data is not present in the list
        if cursor is None:
            print("\nThe data is note present in the list!")
            return
        # If element is present then
        prev.next = cursor.next
        cursor = None

    # Delete at a specified Position
    def deleteAtPosition(self, position):
        cursor = self.head
        i = 0
        prev = None
        while( i < position - 1):
            prev = cursor
            cursor = cursor.next
            i = i + 1
        # print(cursor.data)
        prev.next = cursor.next
        cursor = None
        # print(prev.data)
        # print(cursor.data)

    # Finding the Length iteratively
    def len_iterative(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        print(f"The Length Of linked List is: {count}")
        return count

    # Finding the Length Recursively
    def len_recursive(self, node):
        if(node is None):
            return 0
        return 1 + self.len_recursive(node.next)

    # Swapping the node Basis on Keys
    def node_Swap(self, key1, key2):

        # Keeping Track Of the current Node
        current_1 = self.head
        current_2 = self.head
        # Keeping Track Of the prev Node
        prev_1 = None
        prev_2 = None
        while current_1 and current_1.data != key1:
            prev_1 = current_1
            current_1 = current_1.next
        while current_2 and current_2.data != key2:
            prev_2 = current_2
            current_2 = current_2.next

        if not current_1 or not current_2:
            print("One of the Keys is not present in the List")
            return

        # Checking is current_1 is Head or not
        if prev_1:
            prev_1.next = current_2
        else:
            self.head = current_2

        if prev_2:
            prev_2.next = current_1
        else:
            self.head = current_1

        temp = current_1.next
        current_1.next = current_2.next
        current_2.next = temp

    # Reversing the linked-List Iterative
    def reverse_list_iterative(self):
        current = self.head
        prev = None

        while current:
            print('--------------')
            # temporary variable to keep track of Next without losing
            next = current.next
            current.next = prev

            # if(prev is None):
            #     print("\n Prev: None")
            # else:
            #     print('\n Prev: ', prev.data)
            # print('\n Curn: ', current.data)
            # if(next is None):
            #     print("\n Next: None")
            # else:
            #     print('\n Next: ', next.data)

            prev = current
            current = next
        # print(prev.data)
        self.head = prev

    def reverse_list_recursive(self):
        def _reverse_list_recursive(current, prev):
            if current:
                next_ref = current.next
                current.next = prev
                prev = current
                current = next_ref
                return _reverse_list_recursive(current, prev)
            else:
                return prev
        self.head = _reverse_list_recursive(current = self.head, prev = None)
#--------------------------------------------------------#
# Main Program
linked_list = LinkedList()
linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")
linked_list.append("E")
linked_list.printList()
# linked_list.node_Swap("1", "2")
# print("\n")
# linked_list.printList()
# print("\n")
linked_list.reverse_list_recursive()
print("\n")
linked_list.printList()
# print('\n Inserting Ai At position 5')
# linked_list.insertAtPosition(5,"Ai")
# linked_list.printList()
# print('\n Delete node containing data Ai')
# linked_list.deleteByData("Ai")
# linked_list.printList()
# print('\n Deleting on position 4')
# linked_list.deleteAtPosition(4)
# linked_list.printList()
# print('\n')
# print(linked_list.len_recursive(linked_list.head))