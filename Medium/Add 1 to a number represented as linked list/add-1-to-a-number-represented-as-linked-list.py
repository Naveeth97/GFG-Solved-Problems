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
        
        # if head.data == 9 and head.next == None:
        #     head.data += 1
        #     return head
        
        curr = self.reverse(head)
        reverse_list = self.endOnes(curr)
        
        
        return self.reverse(reverse_list)
        
    def reverse(self, head):
        
        dummy = Node(1)
        
        temp = dummy
        
        res = head
        lis = []
        
        while res != None:
            lis.append(res.data)
            res = res.next
            
        res = head
        for i in range(len(lis) - 1, -1, -1):
            
            temp.next = Node(lis[i])
            temp = temp.next
            
        # if dummy.next.data == 0:
        #     dummy.next.data += 1
            
        return dummy.next
        
    def endOnes(self, head):
        
        temp = head
        
        while temp != None:
            
            if temp.data < 9:
                temp.data += 1
                return head
            else:
                if temp.data == 9 and temp.next is None:
                    temp.data += 1
                else:
                    temp.data = 0
                
            temp = temp.next
                
                
        return head
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
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
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends