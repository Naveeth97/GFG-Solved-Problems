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
        
        zeros = 0
        ones = 0
        twos = 0
        
        temp = head
        
        while temp != None:
            
            if temp.data == 0:
                zeros += 1
            elif temp.data == 1:
                ones += 1
            else:
                twos += 1
            
            temp = temp.next
            
        temp = head
            
        while head != None:
            
            if zeros > 0:
                head.data = 0
                zeros -= 1
            elif ones > 0:
                head.data = 1
                ones -= 1
            else:
                head.data = 2
                twos -= 1
            
            head = head.next
            
        return temp
            
        
            
    


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