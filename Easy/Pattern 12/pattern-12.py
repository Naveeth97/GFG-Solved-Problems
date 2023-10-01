#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1,N+1):
            for k in range(1,i+1):
                print(k,end=' ')
                
            for z in range(1,N- i):
                print(' ',end=' ')
                
            for z in range(0,N-i):
                print(' ',end=' ')
                
            for k in range(i,0,-1):
                print(k,end=' ')
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