#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    def getSingle(self,arr):
        # code here
        
        res = 0
        
        for i in range(len(arr)):
            
            res ^= arr[i]
            
        return res


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        # k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getSingle(arr)
        print(res)
        t -= 1


# } Driver Code Ends