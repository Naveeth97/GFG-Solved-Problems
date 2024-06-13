#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        # code here 
        a, b, c = 1, 1, 1
        mod = 10**9 + 7
    
        for i in range(3, n + 1):
            d = (a + b) % mod
            a, b, c = b, c, d
    
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))

# } Driver Code Ends