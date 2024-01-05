#User function Template for python3

class Solution:
    def trailingZeroes(self, N):
    	#code here 
    	
    	if(N<5):
    	    return 0
    	
    	count = 0
    	while(N>1):
    	    count += (N//5)
    	    N//=5
    	    
    	return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input()) 
        ob = Solution()
        ans = ob.trailingZeroes(N)
        print(ans)
# } Driver Code Ends