#User function Template for python3

class Solution:
    def printDiamond(self, N):
        # Code here
        for i in range(N):
            
            for _ in range(N-i-1):
                print(' ',end='')
                
            for _ in range(i+1):
                print('*',end=' ')
                
                
            print()
        
        for i in range(N,0,-1):
            
            for _ in range(i,N):
                print(' ',end='')
                
            for _ in range(i,0,-1):
                print('*',end=' ')
                
            print()
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printDiamond(N)
# } Driver Code Ends