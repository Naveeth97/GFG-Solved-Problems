#User function Template for python3
class Solution:
	def setBits(self, N):
		# code here
		if N == 0:
		    return N
		    
		cnt = 0
		
		while (N & (N - 1)) != 0:
		    
		    cnt += 1
		    N = N & (N - 1)
		    
		return cnt + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)




# } Driver Code Ends