#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
    	#code here 
    	p = 2
    	res_prime = []
    	prime = [True] * (N+1)
    	while(p*p <=N):
    	    
    	    if(prime[p] == True):
    	        for i in range(p*p,N+1,p):
    	           prime[i] = False
    	    p+=1
    	 
    	for j in range(2,N+1):
    	    if(prime[j]):
    	        res_prime.append(j)
    	return res_prime
    	        
    	        
    	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends