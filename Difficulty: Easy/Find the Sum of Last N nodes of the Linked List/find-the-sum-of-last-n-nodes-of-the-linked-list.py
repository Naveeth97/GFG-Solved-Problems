class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        len = 0
        temp = head
        while temp:
            len += 1
            temp = temp.next
        
        start_pos = len - n
        sum = 0
        temp = head
        index = 0
        while temp:
            if index >= start_pos:
                sum += temp.data
            temp = temp.next
            index += 1
        return sum
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0])
    for i in range(1, t + 1):
        arr = list(map(int, data[2 * i - 1].split()))
        n = int(data[2 * i])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        ob = Solution()
        print(ob.sumOfLastN_Nodes(head, n))

# } Driver Code Ends