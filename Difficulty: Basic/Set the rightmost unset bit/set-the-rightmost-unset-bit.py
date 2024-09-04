#User function Template for python3
class Solution:
    def setBit(self, n):
        # code here
        
        return n | (n + 1)





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())

        ob = Solution()
        ans = ob.setBit(N)
        print(ans)

# } Driver Code Ends