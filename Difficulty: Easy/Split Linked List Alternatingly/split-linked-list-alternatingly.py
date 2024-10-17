#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        
        temp_head1 = head
        temp_head2 = head.next
        
        head1 = temp_head1
        head2 = temp_head2
        
        while (temp_head1 != None and temp_head2 != None):
            
            temp_head1.next = temp_head2.next
            temp_head1 = temp_head1.next
            
            if temp_head1 == None:
                temp_head2 = None
                break
            
            temp_head2.next = temp_head1.next
            temp_head2 = temp_head2.next
            
        return [head1, head2]
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends