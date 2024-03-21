#User function Template for python3

class Solution:
    def countZeroes(self, arr, n):
        # code here
        if(arr[0] == 0):
            return n
        
        count = 0
        res = 0
        
        low = 0
        high = n - 1
        
        while(low <= high):
            
            mid = (low + high)//2
            
            if(arr[mid] == 0):
                
                res = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return n - res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countZeroes(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends