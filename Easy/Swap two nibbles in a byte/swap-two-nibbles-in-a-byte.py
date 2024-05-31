#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        # code here 
        
        a = n % 16
        b = n / 16
        
        return int(a * 16 + b)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends