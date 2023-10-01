#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        pat = 1
        for i in range(1,N+1):
            
            for _ in range(i):
                print(pat,end=' ')
                pat += 1
            print()
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends