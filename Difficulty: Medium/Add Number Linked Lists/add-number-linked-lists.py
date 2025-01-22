#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def addTwoLists(self, num1, num2):
        # code here
        
        num1 = self.reverseLL(num1)
        num2 = self.reverseLL(num2)
        
        result_head = Node(-1)
        traverse_head = result_head
        
        carry = 0
        
        while num1 != None and num2 != None:
            
            sum = num1.data + num2.data + carry
            
            traverse_head.next = Node(sum % 10)
            
            carry = sum // 10;
            
            traverse_head = traverse_head.next
            
            num1 = num1.next
            num2 = num2.next
            
        while num1 != None:
            
            sum = num1.data + carry
            
            traverse_head.next = Node(sum % 10)
            
            carry = sum // 10
            
            traverse_head = traverse_head.next
            
            num1 = num1.next
            
        while num2 != None:
            
            sum = num2.data + carry
            
            traverse_head.next = Node(sum % 10)
            
            carry = sum // 10
            
            traverse_head = traverse_head.next
            
            num2 = num2.next
            
        if (carry != 0):
            
            
            traverse_head.next = Node(carry)
            traverse_head = traverse_head.next
    
            
        
        result_head = self.reverseLL(result_head.next)
        
        while result_head.data == 0:
            
            result_head = result_head.next
        
        return result_head
            
    def reverseLL(self, curr):
        
        prev = None
        
        while (curr != None):
            
            front = curr.next
            
            curr.next = prev
            
            prev = curr
            
            curr = front
            
        return prev
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):

        arr1 = (int(x) for x in input().split())
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)

        arr2 = (int(x) for x in input().split())
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)

        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
        print("~")

# } Driver Code Ends