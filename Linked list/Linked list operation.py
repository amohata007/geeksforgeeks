#Like arrays, Linked List is a linear data structure. Unlike arrays,
# linked list elements are not stored at a contiguous location; the elements are linked using pointers.
class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            st = ''
            while temp:
                st += str(temp.data) + '-->'
                temp = temp.next
            print(st)




var = LinkedList()
var.insert_at_beginning(10)
var.insert_at_beginning(20)
var.insert_at_beginning(30)
var.print_LL()