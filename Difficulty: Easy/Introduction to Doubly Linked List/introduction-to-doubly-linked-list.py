#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    
    head = None
    temp = head;
    
    def constructDLL(self, arr):
        # Code here
        Solution.head = None
        
        for i in range(len(arr)):
            self.createNode(arr[i])
            
        return Solution.head
            
    def createNode(self, data):
        
        newNode = Node(data)
        
        if Solution.head is None:
            Solution.head = newNode
            Solution.temp = Solution.head
        else:
            back = Solution.temp
            Solution.temp.next = newNode
            Solution.temp = Solution.temp.next
            Solution.temp.prev = back
            
            
        
        
        

#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructDLL(arr)
        while res:
            print(res.data, end = ' ')
            res = res.next
        print()
# } Driver Code Ends