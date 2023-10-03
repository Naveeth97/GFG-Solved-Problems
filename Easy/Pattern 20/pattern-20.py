#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        space = (2*N) - 2
        for i in range(N):
            
            for _ in range(i+1):
                print('*',end='')
                
            for _ in range(space):
                print(' ',end='')
                
            for _ in range(i+1):
                print('*',end='')
            print()
            space -= 2
            
        space = 1
        for i in range(N,1,-1):
            
            for _ in range(i-1):
                print('*',end='')
                
            for _ in range(2*space):
                print(' ',end='')
                
            for _ in range(i-1):
                print('*',end='')
                
            print()
            space +=1
            
        


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