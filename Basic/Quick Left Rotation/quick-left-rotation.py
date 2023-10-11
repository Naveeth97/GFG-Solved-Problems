class Solution:
    
    def reverserotate(self,arr,start,end):
        while(start<=end):
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1
    def leftRotate(self, arr, k, n):
        # Your code goes here
        #Time Complexity: O(n)
        if(k == 0):
            return arr
        if(k>n):
            k = k%n
        self.reverserotate(arr,0,k-1)
        self.reverserotate(arr,k,n-1)
        self.reverserotate(arr,0,n-1)
        
        return arr

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends