#Like arrays, Linked List is a linear data structure. Unlike arrays,
# linked list elements are not stored at a contiguous location; the elements are linked using pointers.

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def print_LL(self):
        temp = self.head
        st = ''
        if self.head is None:
            print("Linked List is empty.")
        else:
            while temp:
                pattern = ''
                if temp.next:
                    pattern = '-->'
                st += str(temp.data) + pattern
                temp = temp.next
            print(st)

    def count_LL(self):
        cnt = 0
        temp = self.head
        while temp:
            cnt+=1
            temp = temp.next
        print(cnt)

var = LinkedList()
var.insert_at_beginning(10)
var.insert_at_beginning(20)
var.insert_at_beginning(30)
var.insert_at_beginning(40)
var.insert_at_end(25)
var.insert_at_end(100)
var.count_LL()
var.print_LL()








