#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N,0,-1):
            #leading space
            for _ in range(i,N):
                print(' ',end=' ')
            
            #printing the start patter
            for _ in range(2*i-1,0,-1):
                print('*',end='')
            
            #trailing space
            
            for _ in range(i,N):
                print(' ',end=' ')
            print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends