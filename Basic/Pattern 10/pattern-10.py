#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N):
            for _ in range(i+1):
                print('*',end=' ')
            print()
        
        for i in range(N-1,0,-1):
            for _ in range(i,0,-1):
                print('*',end=' ')
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