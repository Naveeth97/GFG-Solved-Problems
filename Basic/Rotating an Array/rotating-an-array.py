#User function Template for python3

class Solution:
    def reverserotate(self,arr,start,end):
        while(start<=end):
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start +=1
            end -=1
        
    def leftRotate(self, arr, n, d):
        # code here
        #Time complexity: O(n)
        if(d == 0):
            return arr
            
        if(d>n):
            d -= n
            
        self.reverserotate(arr,0,d-1)
        self.reverserotate(arr,d,n-1)
        self.reverserotate(arr,0,n-1)
        
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, n, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends