#User function Template for python3

class Solution:
    def trailingZeroes(self, N):
    	#code here 
    	count = 0
    	if(N<4):
    	    return 0
    	i = 5
    	while(N/i>=1):
    	    count += int(N/i)
    	    i*=5
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