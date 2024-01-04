#User function Template for python3

class Solution:
	def AllPrimeFactors(self, N):
		# Code here
		lis = []
		i = 2
		while(N>1):
		    while(N%i == 0):
		        if i not in lis:
		            lis.append(i)
		        N//=i
		    i+=1
		    
		return lis
		
		    
		    
		        
		        
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.AllPrimeFactors(N)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends