#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import math
class Solution:
    def print_divisors(self, N):
        # code here
        
        lis = []
        
        for i in range(1, int(math.sqrt(N)) + 1):
            
            if N % i == 0:
                lis.append(i)
                
                if (N / i != i):
                    lis.append(int(N / i))
                    
        lis.sort()
        
        for i in lis:
            print(i, end = ' ')
        # return lis

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        ob.print_divisors(N)
        print()
# } Driver Code Ends