# #Like arrays, Linked List is a linear data structure. Unlike arrays,
# # linked list elements are not stored at a contiguous location; the elements are linked using pointers.

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node    #to assign new node to head

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:   #if temp.next exist keep looping and if it gets none means if reached to the last element which we require
            temp = temp.next
        temp.next = Node(data)

    def count_LL(self):
        cnt = 0
        temp = self.head
        while temp:
            cnt+=1
            temp = temp.next
        return cnt

    def insert_at_index(self,index,data):
        if index < 0 or index > self.count_LL():
            raise Exception("Invalid Index")
        if index==0:
            self.insert_at_beginning(data)
            return
        temp = self.head
        cnt=0
        while temp:
            if cnt== index -1:
                node = Node(data,temp.next)
                temp.next = node
                break
            temp = temp.next
            cnt +=1


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

    def remove_at_index(self,index):
        if index<0 or index>self.count_LL():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        temp = self.head
        cnt=0
        while temp:
            if cnt==index-1:
                temp.next = temp.next.next
                break
            temp=temp.next
            cnt+=1

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    # def appendLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    #     # add your logic here
    #     curr = list1
    #     while curr.next != None:
    #         curr = curr.next
    #     curr.next = list2
    #     return list1

var = LinkedList()
var.insert_at_beginning(10)
var.insert_at_beginning(20)
var.insert_at_beginning(30)
var.insert_at_beginning(40)
var.insert_at_end(25)
var.insert_at_end(100)
var.insert_at_index(1,99)
var.insert_at_index(7,11)

var.print_LL()
var.remove_at_index(2)
var.remove_at_index(5)
var.print_LL()

var = LinkedList()
var.insert_values(["abhishek","mohata","hey","there"])
var.print_LL()







# class Node:
#     def __init__(self,data=None,next=None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert_at_beginning(self,data):
#         node = Node(data,self.head)
#         self.head = node
#
#     def count_LL(self):
#         cnt = 0
#         temp = self.head
#         while temp:
#             cnt+=1
#             temp = temp.next
#         return cnt
#
#     def insert_at_end(self,data):
#         if self.head is None:
#             self.head = Node(data)
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = Node(data)
#
#     def insert_at_index(self,data,index):
#         if index<0 or index > self.count_LL():
#             raise Exception("Invalid Index")
#
#         if index==0:
#             self.insert_at_beginning(data)
#             return
#
#         cnt=0
#         temp = self.head
#         while temp:
#             if cnt == index-1:
#                 node = Node(data,temp.next)
#                 temp.next = node
#                 break
#             temp = temp.next
#             cnt+=1
#
#     def delete_at_index(self,index):
#         if index<0 or index > self.count_LL():
#             raise Exception("Invalid Index")
#         if index==0:
#             self.head = self.head.next
#             return
#         cnt=0
#         temp=self.head
#         while temp:
#             if cnt == index-1:
#                 temp.next = temp.next.next
#                 break
#             cnt+=1
#             temp = temp.next
#     def insert_values(self,values):
#         for value in values:
#             self.insert_at_end(value)
#
#     def value_at_index(self,index):
#         temp=self.head
#         cnt=1
#         while temp:
#             if cnt==index:
#                 print(temp.data)
#                 break
#             temp=temp.next
#             cnt+=1
#
#     def print_LL(self):
#         temp = self.head
#         st = ''
#         if temp is None:
#             print("Empty Linked List.")
#         else:
#             while temp:
#                 pat = ''
#                 if temp.next:
#                     pat = '-->'
#                 st += str(temp.data) + pat
#                 temp = temp.next
#         print(st)
#
# var = LinkedList()
# var.insert_at_beginning(10)
# var.insert_at_beginning(20)
# var.insert_at_beginning(30)
# var.insert_at_beginning(40)
# var.insert_at_end(50)
# var.insert_at_index(15,2)
# var.print_LL()
# var.delete_at_index(0)
# var.print_LL()
# var.count_LL()
# var1 = LinkedList()
# var1.insert_values(['hey','there','how','are','you'])
# var1.print_LL()
# var1.value_at_index(41)
