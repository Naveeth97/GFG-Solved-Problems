#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # code here 
        
        if q < 2 or q > n + n:
            return 0
            
        if q > n:
            
            return 2 * n - q + 1
        
        return q - 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends