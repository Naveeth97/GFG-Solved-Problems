#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        
        # reverse it first
        
        new_head = self.reverse(head)
        
        carry = 1
        temp = new_head
        
        # print(new_head.data)
        
        while temp != None:
            
            sum = carry + temp.data
            temp.data = sum % 10
            carry = sum // 10
            temp = temp.next
            
        head = self.reverse(new_head)
        
        if carry > 0:
            
            temp = Node(carry)
            temp.next = head
            head = temp
            
        return head
        
    def reverse(self, head):
        
        curr = head
        new_head = None
        
        while curr != None:
            
            front_node = curr.next
            curr.next = new_head
            new_head = curr
            curr = front_node
            
        return new_head
        
        
        
            
            
            
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next


def PrintList(head):
    while head:
        print(head.data, end='')
        head = head.next


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        list1 = LinkedList()
        arr = list(map(int, input().strip().split()))
        for i in arr:
            list1.insert(i)

        resHead = Solution().addOne(list1.head)
        PrintList(resHead)
        print()
        print("~")

# } Driver Code Ends