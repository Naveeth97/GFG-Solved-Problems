#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
    #code here
    
        prev_node = None
        curr_node = head
        target_node = Node(x)
        
        while curr_node != None:
            
            if curr_node.data <= target_node.data:
                prev_node = curr_node
                curr_node = curr_node.next
            else:
                break
            
        if curr_node == None:
            prev_node.next = target_node
            target_node.prev = prev_node
            
        elif prev_node == None:
            target_node.next = curr_node
            head = target_node
            
        else:
            
            prev_node.next = target_node
            target_node.prev = prev_node
            
            target_node.next = curr_node
            curr_node.prev = target_node
            
        return head
            
        
            
            
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        values = list(map(int, input().strip().split()))
        head = None
        tail = None

        for value in values:
            if head is None:
                head = Node(value)
                tail = head
            else:
                tail.next = Node(value)
                tail.next.prev = tail
                tail = tail.next

        value_to_insert = int(input().strip())
        solution = Solution()
        head = solution.sortedInsert(head, value_to_insert)
        print_list(head)

        print("~")

# } Driver Code Ends