#User function Template for python3
class Solution:
    def firstElement (self, n):
        # code here 
        if(n == 1 or n  == 2):
            return 1
            
        x = 1 
        y = 1
        for i in range(n - 2):
            
            z = (x + y) % 1000000007
            x = y % 1000000007
            y = z % 1000000007
            
        return z % 1000000007
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends