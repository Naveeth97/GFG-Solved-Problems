#User function Template for python3

class Solution:
    
    def getSingle(self,arr, n):
        # code here
        res =0
        
        for i in arr:
            
            res ^= i
            
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getSingle(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends