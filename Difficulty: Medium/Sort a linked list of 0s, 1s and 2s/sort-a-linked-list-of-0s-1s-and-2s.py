'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''
	
class Solution:
    def segregate(self, head):
        #code here
        
        zeroHead = Node(-1)
        oneHead = Node(-1)
        secHead = Node(-1)
        
        temp_zero = zeroHead
        temp_one = oneHead
        temp_sec = secHead
        
        while (head != None):
            
            if head.data == 0:
                
                temp_zero.next = Node(head.data)
                temp_zero = temp_zero.next
            elif head.data == 1:
                
                temp_one.next = Node(head.data)
                temp_one = temp_one.next
                
            else:
                
                temp_sec.next = Node(head.data)
                temp_sec = temp_sec.next
                
            head = head.next
            
        zeroHead = zeroHead.next
        oneHead = oneHead.next
        secHead = secHead.next
        
        if zeroHead != None:
            
            if oneHead != None:
                
                temp_zero.next = oneHead
                temp_one.next = secHead
            else:
                
                temp_zero.next = secHead
        else:
            
            if oneHead != None:
                
                temp_one.next = secHead
                return oneHead
            else:
                
                return secHead
                
        return zeroHead
    


#{ 
 # Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().segregate(head))
        print("~")

# } Driver Code Ends