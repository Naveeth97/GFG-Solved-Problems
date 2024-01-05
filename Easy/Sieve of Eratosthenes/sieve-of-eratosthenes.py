#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
    	#code here 
        lis = [0] * (N + 1)
        
        i = 2
        while(i * i<=N):
            
            if(lis[i] == 0):
                for j in range(i*i,N + 1,i):
                    lis[j] = 1
            
            i+=1
        primes = []
        i = 2
        while(i<=N):
            if(lis[i] == 0):
                primes.append(i)
            i+=1
                
        return primes
                
            

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